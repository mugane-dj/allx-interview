#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == "__main__":
    total_size = 0
    line_count = 0
    status_codes = {}
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
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
                    print("File size: {}".format(file_size))
                    for k, v in sorted(status_codes.items()):
                        if v > 0:
                            print("{}: {}".format(k, v))
    finally:
        print("File size: {}".format(file_size))
        for k, v in sorted(status_codes.items()):
            if v > 0:
                print("{}: {}".format(k, v))
