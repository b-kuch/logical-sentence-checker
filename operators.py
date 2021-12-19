from __future__ import annotations

from abc import ABC
from abc import abstractmethod
import logging as log

class Operator(ABC):
    @abstractmethod
    def decide(self, values : dict[str, bool]) -> bool:
        ...

    def bracket(self, obj):
        if isinstance(obj, Operand):
            return str(obj.value)
        else:
            return f'({str(obj)})'


class UnaryOperator(Operator):
    def __init__(self, variable : Operator) -> None:
        if (isinstance(variable, list)):
            log.debug(f'variable passed to {self.__class__.__name__} init is a list')
        self.value : Operator or str = variable

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}<{repr(self.value)}>'


class BinaryOperator(Operator):
    def __init__(self, variable1 : Operator or str, variable2 : Operator or str) -> None:
        if (isinstance(variable1, list)):
            log.debug(f'variable1 passed to {self.__class__.__name__} init is a list')
        if (isinstance(variable2, list)):
            log.debug(f'variable2 passed to {self.__class__.__name__} init is a list')
        self.value1 : Operator or str = variable1
        self.value2 : Operator or str = variable2

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}<{repr(self.value1)}, {repr(self.value2)}>'


class Operand(UnaryOperator):
    def __init__(self, variable: str) -> None:
        self.value = variable.strip()

    def decide(self, values: dict[str, bool]) -> bool:
        return values[self.value]

    def __str__(self) -> str:
        return str(self.bracket(self.value))

    def __eq__(self, o : Operand) -> bool:
        if isinstance(o, Operand):
            return self.value == o.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)


class Not(UnaryOperator):
    def decide(self, values: dict[str, bool]) -> bool:
        return not self.value.decide(values)

    def __str__(self) -> str:
        return f'not {self.bracket(self.value)}'
  

class And(BinaryOperator):
    def decide(self, values: dict[str, bool]) -> bool:
        return self.value1.decide(values) and self.value2.decide(values)

    def __str__(self) -> str:
        return f'{self.bracket(self.value1)} and {self.bracket(self.value2)}'


class Or(BinaryOperator):
    def decide(self, values: dict[str, bool]) -> bool:
        return self.value1.decide(values) or self.value2.decide(values)

    def __str__(self) -> str:
        return f'{self.bracket(self.value1)} or {self.bracket(self.value2)}'
