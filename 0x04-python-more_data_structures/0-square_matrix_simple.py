#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res =[[row ** 2 for row in l_elmnt] for l_elmnt in matrix]
    return res
