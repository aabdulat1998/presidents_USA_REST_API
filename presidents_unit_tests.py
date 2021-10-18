# This is a module that tests for the presidents of the US

import pytest
from main import president_search


@pytest.mark.parametrize("president", [
    "Washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monroe",
    "Adams",
    "Jackson",
    "Buren",
    "Harrison",
    "Tyler",
    "Polk",
    "Taylor",
    "Fillmore",
    "Pierce",
    "Buchanan",
    "Lincoln",
    "Johnson",
    "Grant",
    "Hayes",
    "Garfield",
    "Cleveland",
    "McKinley",
    "Roosevelt",
    "Taft",
    "Wilson",
    "Harding",
    "Coolidge",
    "Roosevelt",
    "Truman",
    "Eisenhower",
    "Kennedy",
    "Johnson",
    "Nixon",
    "Ford",
    "Carter",
    "Reagan",
    "Bush",
    "Clinton",
    "Obama",
    "Trump",
    "Biden",
])
def test_presidents(president):
    assert [s for s in president_search() if president in s]
