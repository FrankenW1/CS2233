import pytest
from quiz import quiz1

x = ['a', 'z']


def test(lst):
    quiz1.first(x)
    assert quiz1.first(x) == 'a'
