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
