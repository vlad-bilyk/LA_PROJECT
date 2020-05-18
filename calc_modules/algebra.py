import math


def mat_dist_sq(m1, m2):
    """
    Distance between two matrices: square root of sum of squared differences
    :param m1: 2d array
    :param m2: 2d array
    :return: int - distance
    """
    d = 0

    for col1, col2 in zip(m1, m2):
        for el1, el2 in zip(col1, col2):
            d += pow(el1 - el2, 2)

    return math.sqrt(d)


def mat_dist_abs(m1, m2):
    """
    Distance between two matrices: sum of absolute value of differences
    :param m1: 2d array
    :param m2: 2d array
    :return: int - distance
    """
    d = 0

    for col1, col2 in zip(m1, m2):
        for el1, el2 in zip(col1, col2):
            d += abs(el1 - el2)

    return d


def add_matices(m1, m2):
    """

    :param m1:
    :param m2:
    :return:
    """
    if len(m1) == 0:
        return m2
    elif len(m2) == 0:
        return m1
    mat = [[None for i in range(len(m1[0]))] for j in range(len(m1)) ]

    for col1, col2 in zip(range(len(m1)), range(len(m2))):
        for el1, el2 in zip(range(len(m1[col1])), range(len(m2[col2]))):
            new_el = m1[col1][el1] + m2[col2][el2]
            mat[col1][el1] = new_el

    return mat
