import math
from decimal import Decimal

import pytest

from lib.rpn_calculator import rpn_calculator


def test_failure_number_of_operands():

    with pytest.raises(ValueError):
        rpn_calculator("2 3")

    with pytest.raises(ValueError):
        rpn_calculator("2 3 + *")

    with pytest.raises(ValueError):
        rpn_calculator("2 3 sqrt")

def test_constants():
    assert float(rpn_calculator("PI")) == pytest.approx(3.14, 0.01)
    assert float(rpn_calculator("E")) == pytest.approx(math.e, 0.01)

def test_one_operand_operators():
    assert rpn_calculator("1 sqrt") == Decimal('1'), "squared root of 1 is 1"
    assert rpn_calculator("4 sqrt") == Decimal('2'), "squared root of 4 is 2"
    assert rpn_calculator("9 sqrt") == Decimal('3'), "squared root of 9 is 3"

    assert rpn_calculator("10 log10") == Decimal('1'), "log10 of 10 is 1"

def test_two_operand_operators_simple():
    assert rpn_calculator("2 3 +") == Decimal('5'), "2 3 + => 2 + 3 = 5"
    assert rpn_calculator("2 3 -") == Decimal('-1'), "2 3 - => 2 - 3 = -1"
    assert rpn_calculator("3 2 *") == Decimal('6'), "3 2 * => 3 * 2 = 6"
    assert rpn_calculator("3 2 /") == Decimal('1.5'), "3 2 / => 3 / 2 = 1.5"
    assert rpn_calculator("3 2 %") == Decimal('1'), "3 2 % => 3 % 2 = 1"
    assert rpn_calculator("2 2 **") == Decimal('4'), "2 2 ** => 2 ** 2 = 4"
    assert rpn_calculator("2 3 **") == Decimal('8'), "2 3 ** => 2 ** 3 = 8"


def test_two_operand_operators_complex():
    # (2 + 3) * 4 = 20
    assert rpn_calculator("2 3 + 4 *") == Decimal('20'), "2 3 + 4 * => (2 + 3) * 4 = 20"
    assert rpn_calculator("4 2 3 + *") == Decimal('20'), "4 2 3 + * => 4 * (2 + 3) = 20"


    # (1 + 2) * (3 + 4) = 21
    assert rpn_calculator("1 2 + 3 4 + *") == Decimal('21'), "1 2 + 3 4 + * => (1 + 2) * (3 + 4) = 21"
