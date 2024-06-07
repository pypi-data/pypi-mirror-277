# Copyright (c) 2024, InfinityQ Technology, Inc.

import abc
import enum
from typing import List, Optional, Tuple
import numpy as np
from numpy._typing import NDArray

class Vtype(str, enum.Enum):
    """
    All variables types currently supported by the solver
    """

    BINARY = 'binary'
    BIPOLAR = 'bipolar'
    INTEGER = 'integer'
    CONTINUOUS = 'continuous'

    def __str__(self) -> str:
        return str(self.value)

class VariableVector(abc.ABC):
    """
    Object That represent a vector of variable to be optimized.
    """
    
    # Disable NumPy's (ufuncs) to avoid unintended operations on this class with array
    __array_ufunc__ = None
    def __init__(self, name: str, size: int) -> None:
        if size < 1:
            raise ValueError("Variable vector size cannot be less than 1")

        self._name = name
        self._size = size


    def size(self) -> int:
        """
        :return: size of this vector.
        """
        return self._size


    def name(self) -> str:
        """
        :return: Name of this variable vector.
        """
        return self._name
    
    def __mul__(self, other):
        return mul_dispatcher(self, other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        return add_dispatcher(self, other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        return sub_dispatcher(self, other)

    @abc.abstractmethod
    def vtype(self) -> Vtype:
        """
        :return: Type of variable in the vector.
        """


    @abc.abstractmethod
    def variable_types_as_list(self) -> str:
        """
        :return: Generate a string of 'b', 'i' or 'c' depending on the variable type
        """


    @abc.abstractmethod
    def variable_bounds(self) -> NDArray:
        """
        :return: The variable bounds associated to this variable vector
        """


class BinaryVariableVector(VariableVector):
    def vtype(self) -> Vtype:
        return Vtype.BINARY


    def variable_types_as_list(self) -> str:
        return "b" * self.size()


    def variable_bounds(self) -> NDArray:
        return np.tile(np.array([0,1], dtype=np.float32), (self._size, 1))


# This class violate the Liskov Substitution Principle because it raise error in some of
# the method it need to implement. This is somewhat fine for now but should be fix soon.
class BipolarVariableVector(VariableVector):
    def vtype(self) -> Vtype:
        return Vtype.BIPOLAR

    def variable_types_as_list(self) -> str:
        raise ValueError("Cannot set variable types as a list for 'bipolar' variable type")

    def variable_bounds(self) -> NDArray:
        raise ValueError("Cannot define variable bounds for 'bipolar' variable type")


class IntegerVariableVector(VariableVector):
    def __init__(self, name: str, size: int, variable_bounds: List[Tuple[int, int]]) -> None:
        super().__init__(name, size)

        if len(variable_bounds) != self.size():
            raise ValueError("variable_bounds need to be the same length as variable size")

        self._variable_bounds = np.array(variable_bounds, dtype=np.float32)


    def vtype(self) -> Vtype:
        return Vtype.INTEGER


    def variable_types_as_list(self) -> str:
        return "i" * self.size()


    def variable_bounds(self) -> NDArray:
        return self._variable_bounds

class ContinuousVariableVector(VariableVector):
    def __init__(self, name: str, size: int, variable_bounds: List[Tuple[int, int]]) -> None:
        super().__init__(name, size)

        if len(variable_bounds) != self.size():
            raise ValueError("variable_bounds need to be the same length as variable size")

        self._variable_bounds = np.array(variable_bounds, dtype=np.float32)


    def vtype(self) -> Vtype:
        return Vtype.CONTINUOUS


    def variable_types_as_list(self) -> str:
        return "c" * self.size()


    def variable_bounds(self) -> NDArray:
        return self._variable_bounds



class Term:
    # Disable NumPy's (ufuncs) to avoid unintended operations on this class with array
    __array_ufunc__= None
    
    def __init__(self,
        v1: VariableVector,
        v2: Optional[VariableVector],
        coeff: np.ndarray):
        self._v1 = v1
        self._v2 = v2
        self._coeff = coeff
    
    def __mul__(self, other):
        return mul_dispatcher(self, other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        return add_dispatcher(self, other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        return sub_dispatcher(self, other)
        
class Expression:
    def __init__(self, terms: List[Term]):
        self._terms = terms
    
    def __mul__(self, other):
       return mul_dispatcher(self, other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __add__(self, other):
        return add_dispatcher(self, other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        return sub_dispatcher(self, other)

def add_dispatcher(lhs, rhs):
    if isinstance(lhs, VariableVector) and isinstance(rhs, VariableVector):
        return Expression(terms=[Term(v1=lhs, v2=None, coeff=np.ones((lhs._size), dtype=np.float32)),
                                    Term(v1=rhs, v2=None, coeff=np.ones((rhs._size), dtype=np.float32))])
    if isinstance(lhs, VariableVector) and isinstance(rhs, Term):
        return Expression(terms=[Term(v1=lhs, v2=None, coeff=np.ones((lhs._size), dtype=np.float32)), rhs])
    if isinstance(lhs, VariableVector) and isinstance(rhs, Expression):
        return Expression(terms= [Term(v1=lhs, v2=None, coeff=np.ones((lhs._size), dtype=np.float32))] + rhs._terms)
    if isinstance(lhs, Term) and isinstance(rhs, Term):
            return Expression(terms=[lhs, rhs])
    if isinstance(lhs, Term) and isinstance(rhs, Expression):
        return Expression(terms=[lhs] + rhs._terms)
    if isinstance(lhs, Expression) and isinstance(rhs, Expression):
            return Expression(terms=lhs._terms + rhs._terms)
    if isinstance(rhs, (int, float)):
        # TODO store it for constraint
        return lhs
    return NotImplemented

def mul_dispatcher(lhs, rhs):
    if isinstance(lhs, VariableVector) and isinstance(rhs, VariableVector):
            return Term(v1=lhs, v2=rhs, coeff=np.ones((lhs._size, rhs._size), dtype=np.float32))
    if isinstance(lhs, VariableVector) and isinstance(rhs, np.ndarray):
        if len(rhs) != lhs._size or rhs.ndim != 1:
            raise ValueError(f"Coefficient array size doesn't match the size of the VariableVector.")
        return Term(v1=lhs, v2=None, coeff=rhs)
    if isinstance(lhs, VariableVector) and isinstance(rhs, (int, float)):
        return Term(v1=lhs, v2=None, coeff=np.full(lhs._size, rhs, dtype=np.float32))
    if isinstance(lhs, VariableVector) and isinstance(rhs, Term):
        if rhs._v2 is not None:
            raise ValueError(f"The expression degree is too hight.")
        return Term(v1=rhs._v1, v2=lhs, coeff=np.array([[element] * lhs._size for element in rhs._coeff], dtype=np.float32 ))
    

    if isinstance(lhs, Term) and isinstance(rhs, Term):
            if rhs._v2 is not None or lhs._v2 is not None:
                raise ValueError(f"The expression degree is too hight.")
            return Term(v1=lhs._v1, v2=rhs._v1, coeff=np.outer(lhs._coeff, rhs._coeff))
    if isinstance(lhs, Term) and isinstance(rhs, np.ndarray):
        if lhs._v2 is None and (rhs.ndim != 1 or len(rhs) != lhs._v1._size) or \
            lhs._v2 is not None and (rhs.ndim != 2 or len(rhs) != lhs._v1._size or len(rhs[0]) != lhs._v2._size):
                raise ValueError(f"Coefficient matrix size doesn't match the size of the term.")
        return Term(v1=lhs._v1, v2=lhs._v2, coeff=rhs*lhs._coeff)
    if isinstance(lhs, Term) and isinstance(rhs, (int, float)):
        return Term(v1= lhs._v1, v2=lhs._v2, coeff=lhs._coeff*rhs)
    

    if isinstance(lhs, Expression) and isinstance(rhs, (int, float, VariableVector, Term)):
            return Expression(terms=[term*rhs for term in lhs._terms])
    return NotImplemented

def sub_dispatcher(lhs, rhs):
    if isinstance(rhs, (VariableVector, Term, Expression)):
        return lhs + rhs*-1
    if isinstance(rhs, (int, float)):
        # TODO store it for constraint
        return lhs
    return NotImplemented
