#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiply matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Return: multiplication of a and b
    """
    return numpy.matmul(m_a, m_b)
