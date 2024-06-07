# pylint: disable=too-few-public-methods

"""
This module defines classes to represent SQL expressions, including
columns, literals, and operations.
"""

from typing import Union


class Column:
    """
    Represents a column in a SQL query.

    Attributes:
        name (str): The name of the column.
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name


class Literal:
    """
    Represents a literal value in a SQL query.

    Attributes:
        value (Union[int, float, str]): The value of the literal.
    """

    def __init__(self, value: Union[int, float, str]):
        self.value = value

    def __str__(self) -> str:
        if isinstance(self.value, str):
            return f"'{self.value}'"
        return str(self.value)


class Operation:
    """
    Represents an operation in a SQL query.

    Attributes:
        left (Column): The left operand of the operation.
        operator (str): The operator of the operation (e.g., '=', '>', '<').
        right (Literal): The right operand of the operation.
    """

    def __init__(self, left: Column, operator: str, right: Literal):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f"{self.left} {self.operator} {self.right}"
