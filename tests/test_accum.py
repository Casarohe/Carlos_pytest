import pytest
from stuff.accum import Accumulator

# Fixtures
@pytest.fixture
def accum():
    return Accumulator()


@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0


# Tests
@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2

@pytest.mark.accumulator
def test_accumulator_private_property(accum):
    with pytest.raises(AttributeError, match = r"can't set attribute") as attrer:
        accum.count = 10