# Copyright (c) 2024, InfinityQ Technology, Inc.

from typing import List, Tuple

import numpy as np
from titanq._model.variable import Expression, Term, VariableVector


def extract_bias_vector_and_weight_matrix_from_expression(expr: Expression, variables:List[VariableVector]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Extracts the bias vector and weight matrix from an expression.

    This function processes an expression and a list of variable vectors to extract the bias vector and weight matrix. 
    The bias vector and weight matrix are initialized based on the number of variables and then populated based on the terms in the expression.

    Parameters:
    ----------
    expr : Expression
        The expression from which to extract the bias vector and weight matrix. 
        It can be an instance of `Expression`, `Term`, or `VariableVector`.
    
    variables : List[VariableVector]
        A list of variable vectors used in the expression. 
        Each variable vector's size contributes to the overall size of the bias vector and weight matrix.

    Returns:
    -------
    tuple
        A tuple containing:
        - weight_matrix (numpy.ndarray): A 2D array representing the weight matrix.
        - bias_vector (numpy.ndarray): A 1D array representing the bias vector.

    Notes:
    -----
    - If the expression is a `VariableVector`, it is converted to a `Term`.
    - If the expression is a `Term`, it is converted to an `Expression`.
    - The function assumes the coefficient matrix is symmetric when both `v1` and `v2` are present in a term.
    """
    variables_index={}
    nbr_of_variables=0
    for var in variables:
        variables_index[var] = nbr_of_variables
        nbr_of_variables += var._size

    bias_vector= np.zeros(nbr_of_variables, dtype=np.float32)
    weight_matrix=np.zeros((nbr_of_variables, nbr_of_variables), dtype=np.float32)
    if isinstance(expr, VariableVector):
        expr= Term(expr, None, np.ones(expr._size, dtype=np.float32))
    if isinstance(expr, Term):
        expr= Expression(terms=[expr])
    for term in expr._terms:
        index_v1 = variables_index[term._v1]
        if term._v2 is None:
            bias_vector[index_v1:index_v1+term._v1._size] += term._coeff
        else:
            index_v2 = variables_index[term._v2]
            weight_matrix[index_v1 : index_v1 + term._v1._size, index_v2 : index_v2 + term._v2._size] = term._coeff
            weight_matrix[index_v2 : index_v2 + term._v2._size, index_v1 : index_v1 + term._v1._size] = term._coeff.T

    return weight_matrix, bias_vector