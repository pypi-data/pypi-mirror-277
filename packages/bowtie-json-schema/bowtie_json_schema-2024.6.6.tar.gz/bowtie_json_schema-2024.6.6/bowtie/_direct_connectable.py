"""
Direct connectables do not really connect anywhere and just operate in-memory.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from importlib import metadata
from typing import TYPE_CHECKING, Any, Generic
import platform

from attrs import asdict, field, frozen, mutable
from referencing.jsonschema import EMPTY_REGISTRY
from url import URL

from bowtie._commands import CaseResult, Started, StartedDialect, TestResult
from bowtie._core import Connection, Dialect, ImplementationInfo
from bowtie._registry import E_co, SchemaCompiler

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Callable, Iterable

    from jsonschema import ValidationError
    from jsonschema.protocols import Validator
    from referencing.jsonschema import Schema, SchemaRegistry

    from bowtie._commands import Message
    from bowtie._connectables import ConnectableId


class NoDirectConnection(Exception):
    @classmethod
    def check(cls, _: Any, __: Any, id: ConnectableId):
        if id not in IMPLEMENTATIONS:
            raise cls(id)

    def __str__(self):
        return f"No direct connection can be made to {self.args[0]!r}."


def not_yet_connected(schema: Schema, registry: SchemaRegistry):
    def _not_yet_connected(instance: Any):
        raise RuntimeError("Not yet connected!")

    return _not_yet_connected


@mutable
class Unconnection(Generic[E_co]):

    _info: ImplementationInfo = field(
        repr=lambda value: f"{value.language}-{value.name}",
        alias="info",
    )
    _compile: Callable[[Dialect], SchemaCompiler[E_co]] = field(
        repr=False,
        alias="compile",
    )
    _dialect: Dialect = Dialect.latest()
    _for_current_dialect: SchemaCompiler[E_co] = not_yet_connected

    async def request(self, message: Message) -> Message:
        """
        Unpack the request and call our implementation.

        Call us, we always respond (so we never return ``None``).
        """
        match message:  # FIXME: Should request take Commands?
            case {"cmd": "start", "version": 1}:
                started = Started(
                    implementation=self._info.serializable(),  # FIXME
                    version=1,
                )
                return asdict(started)
            case {"cmd": "dialect", "dialect": uri}:
                self._dialect = Dialect.by_uri()[URL.parse(uri)]
                self._for_current_dialect = self._compile(self._dialect)
                return asdict(StartedDialect.OK)
            case {"cmd": "run", "seq": seq, "case": case}:
                schema = case["schema"]
                registry = EMPTY_REGISTRY.with_contents(
                    case.get("registry", {}).items(),
                    default_specification=self._dialect.specification(),
                )
                errors_for = self._for_current_dialect(schema, registry)
                results = [
                    TestResult(
                        valid=(
                            next(iter(errors_for(test["instance"])), None)
                            is None
                        ),
                    )
                    for test in case["tests"]
                ]
                return {  # FIXME: Bleh this is not SeqResult
                    "seq": seq,
                    **CaseResult(results=results).serializable(),
                }
            case {"cmd": "stop"}:
                return {}
            case _:
                raise RuntimeError(f"Unknown message: {message!r}")

    async def poison(self, message: Message) -> None:
        """
        Do nothing.
        """


def python_implementation(
    **kwargs: Any,
) -> Callable[
    [Callable[[Dialect], SchemaCompiler[E_co]]],
    Callable[[], Unconnection[E_co]],
]:
    def _python_implementation(
        fn: Callable[[Dialect], SchemaCompiler[E_co]],
    ) -> Callable[[], Unconnection[E_co]]:
        name = kwargs.pop("name", fn.__name__)
        info = ImplementationInfo(
            name=name,
            version=metadata.version(name),
            language="python",
            os=platform.system(),
            os_version=platform.release(),
            language_version=platform.python_version(),
            **kwargs,
        )
        return lambda: Unconnection(compile=fn, info=info)

    return _python_implementation


@python_implementation(
    homepage=URL.parse("https://python-jsonschema.readthedocs.io/"),
    documentation=URL.parse("https://python-jsonschema.readthedocs.io/"),
    issues=URL.parse("https://github.com/python-jsonschema/jsonschema/issues"),
    source=URL.parse("https://github.com/python-jsonschema/jsonschema"),
    dialects=frozenset(
        [
            Dialect.by_short_name()["draft2020-12"],
            Dialect.by_short_name()["draft2019-09"],
            Dialect.by_short_name()["draft7"],
            Dialect.by_short_name()["draft6"],
            Dialect.by_short_name()["draft4"],
            Dialect.by_short_name()["draft3"],
        ],
    ),
)
def jsonschema(dialect: Dialect) -> SchemaCompiler[ValidationError]:
    from jsonschema.validators import (
        validator_for,  # type: ignore[reportUnknownVariableType]
    )

    def compile(
        schema: Schema,
        registry: SchemaRegistry,
    ) -> Callable[[Any], Iterable[ValidationError]]:
        DialectValidator: type[Validator] = validator_for(  # type: ignore[reportUnknownVariableType]
            schema,
            default=validator_for({"$schema": str(dialect.uri)}),
        )
        validator: Validator = DialectValidator(schema, registry=registry)  # type: ignore[reportUnknownVariableType]
        return validator.iter_errors  # type: ignore[reportUnknownMemberType]

    return compile


IMPLEMENTATIONS = {
    "python-jsonschema": jsonschema,
}


@frozen
class Direct:
    """
    A direct connectable connects by simply importing some Python object.

    This is generally going to be suitable only to implementations written in
    Python or to a language where a wrapper (PyO3, CFFI, ...) can expose
    libraries written in the language directly to Python.

    This object represents only the lazy import.
    Connecting will lookup and call the object from the identified location.
    The return value should then be an object which makes use of a specific
    target implementation.
    """

    _id: ConnectableId = field(alias="id", validator=NoDirectConnection.check)

    connector = "direct"

    @asynccontextmanager
    async def connect(self, **kwargs: Any) -> AsyncIterator[Connection]:
        yield IMPLEMENTATIONS[self._id]()
