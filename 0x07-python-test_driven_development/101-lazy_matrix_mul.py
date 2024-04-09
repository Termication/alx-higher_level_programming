#!/usr/bin/python3

"""A module for matrix multiplication"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        np.ndarray: The product of the two matrices.
    """
    return np.matmul(m_a, m_b)
