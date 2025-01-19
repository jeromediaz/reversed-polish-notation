import math
from decimal import Decimal
from typing import List


def rpn_calculator(expression: str) -> Decimal:
    """
    Method to evaluate a Reverse Polish Notation (RPN) expression.

    Args:
        expression (str): Reverse Polish notation expression.

    Returns:
        Decimal: the return value
    """

    local_stack: List[Decimal] = []

    numerical_constants = {
        'PI': Decimal.from_float(math.pi),
        'E': Decimal.from_float(math.e),
    }

    one_operand_operators = {
        'log10': lambda x: x.log10(),
        'sqrt': lambda x: x.sqrt(),
    }

    two_operands_operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '%': lambda x, y: x % y,
                 '**': lambda x, y: x ** y,
                  }

    tokens = expression.split()

    for token in tokens:
        if token in numerical_constants:
            local_stack.append(numerical_constants[token])
            continue

        if token in one_operand_operators:
            if len(local_stack) < 1:
                raise ValueError(f"Invalid operation {token}: not enough operand.")

            x = local_stack.pop()

            result = one_operand_operators[token](x)
            local_stack.append(result)

        elif token in two_operands_operators:
            if len(local_stack) < 2:
                raise ValueError(f"Invalid operation {token}: not enough operands.")

            y = local_stack.pop()
            x = local_stack.pop()

            result = two_operands_operators[token](x, y)
            local_stack.append(result)
        else:
            try:
                local_stack.append(Decimal(token))
            except ValueError:
                raise ValueError(f"Invalid  token: {token}")

    if len(local_stack) != 1:
        raise ValueError("Invalid operation: two many remaining operands.")

    return local_stack[0]