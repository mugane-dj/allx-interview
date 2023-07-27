#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    The function pascal_triangle generates a Pascal's triangle
    with n number of rows.

    :param n: The parameter `n` represents the number of rows in the
              Pascal's triangle that you want to
    generate
    :return: a Pascal's triangle as a list of lists.
             Each inner list represents a row in the triangle, and
             each element in the inner list represents a number in that row.
    """

    triangle = []  # List of lists
    if n > 0:
        # Looping through every row in range 0 -> n
        for row in range(n):
            # Every row in the triangle starts and ends with 1
            curr_row = [1]

            # Append middle elements to current row
            if row > 0:
                for i in range(1, row):
                    # First loop resolves to the sum of elements in index (0,0)
                    # and index (0,1)
                    curr_row.append(triangle[row - 1][i - 1] +
                                    triangle[row - 1][i])
            if row > 0:
                curr_row.append(1)
            triangle.append(curr_row)
    return triangle
