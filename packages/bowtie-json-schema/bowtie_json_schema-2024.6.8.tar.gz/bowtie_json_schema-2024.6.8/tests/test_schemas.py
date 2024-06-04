"""
Test Bowtie's schemas for proper functionality.
"""

import pytest

from bowtie._core import validator_registry

TEST = {
    "description": "a test",
    "instance": 37,
}
ANOTHER_TEST = {
    "description": "another test",
    "instance": "foo",
}


def errors(uri, instance):
    return list(validator_registry().for_uri(uri).errors_for(instance))


@pytest.mark.parametrize(
    "valid, instance",
    [
        (
            True,
            {
                "description": "test group with schema",
                "schema": {},
                "children": [TEST],
            },
        ),
        (
            True,
            {
                "description": "test group with schema and registry",
                "schema": {},
                "registry": {"urn:example": {}},
                "children": [TEST],
            },
        ),
        (
            True,
            {
                "description": "outer test group",
                "children": [
                    {
                        "description": "inner test group",
                        "schema": {},
                        "children": [TEST],
                    },
                ],
            },
        ),
        (
            True,
            {
                "description": "level 3",
                "children": [
                    {
                        "description": "level 2",
                        "children": [
                            {
                                "description": "level 1",
                                "schema": {},
                                "children": [TEST],
                            },
                        ],
                    },
                ],
            },
        ),
        (
            False,
            {
                "description": "test group missing schema everywhere",
                "children": [
                    {
                        "description": "a test",
                        "instance": 37,
                    },
                ],
            },
        ),
        (
            False,
            {
                "description": "duplicated schema",
                "schema": {},
                "children": [
                    {
                        "description": "inner test group",
                        "schema": {},
                        "children": [TEST],
                    },
                ],
            },
        ),
        (
            False,
            {
                "description": "duplicated registry",
                "schema": {},
                "registry": {},
                "children": [
                    {
                        "description": "inner test group",
                        "registry": {"urn:example": {}},
                        "children": [TEST],
                    },
                ],
            },
        ),
        (
            False,
            {
                "description": "nonhomogeneous test group",
                "children": [
                    TEST,
                    {
                        "description": "test group, not test",
                        "children": [ANOTHER_TEST],
                    },
                ],
            },
        ),
        (
            False,
            {
                "description": "test group with invalid registry",
                "schema": {},
                "registry": 37,
                "children": [TEST],
            },
        ),
        (
            False,
            {
                "description": "test group with empty children",
                "schema": {},
                "children": [],
            },
        ),
    ],
)
def test_group(valid, instance):
    got = errors("tag:bowtie.report,2023:models:group", instance)
    assert valid == (not got), got


def test_root_schema():
    canonical_url = "tag:bowtie.report,2023:ihop"
    schema = validator_registry().schema(canonical_url)
    assert schema["$id"] == canonical_url
