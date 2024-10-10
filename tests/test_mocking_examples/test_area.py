import math
from nis import match

import pytest

from source.mocking_examples.area import area_of_circle


def test_area():
    assert  area_of_circle(5) == 5 * 5 * math.pi