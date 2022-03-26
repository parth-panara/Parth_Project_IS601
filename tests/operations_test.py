"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_add_float():
    """Testing the Calculator"""
    assert Addition.add(1.7, 2.5) == 4.2


def test_calculator_operations_subtract():
    """Testing the Calculator"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Multiplication.multiply(1, 1) == 1


def test_calculator_operations_multiply_float():
    """Testing the Calculator"""
    assert Multiplication.multiply(1.5, 2.5) == 3.75


def test_calculator_operations_divide():
    """Testing the Calculator"""
    assert Division.divide(10, 5) == 2

def test_calculator_operations_divide_with_float_value():
    """Testing the Calculator"""
    assert Division.divide(5, 2) == 2.5


def test_calculator_operations_divide_by_zero():
    """Testing the Calculator"""
    assert Division.divide(5, 0) == "Error: Division by zero is not correct"
