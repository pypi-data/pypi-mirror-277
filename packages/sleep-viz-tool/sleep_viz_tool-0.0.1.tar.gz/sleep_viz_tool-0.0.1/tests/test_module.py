import pytest
from sleep_viz_tool.module import add


def test_add():
    res = add(3, 5)
    assert res == 8
