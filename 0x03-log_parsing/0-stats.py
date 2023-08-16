#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


def print_output(status_codes, file_size):
    """
    The function "print_output" prints the status codes
    and their corresponding counts if the count is greater than zero.

    :param status_codes: A dictionary where the keys are status codes
                         (e.g. 200, 404) and the values  are the number
                         of occurrences of each status code
    :param file_size: The file_size parameter is the size of a file in bytes
    """
    print("File size: {}".format(file_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))


total_size = 0
line_count = 0
status_codes = {}

try:
    while True:
        line = sys.stdin.readline().strip()
        parts = line.split()

        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    total_size += file_size
                    status_codes[status_code] = status_codes.get(
                        status_code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_output(status_codes, total_size)
finally:
    print_output(status_codes, total_size)
