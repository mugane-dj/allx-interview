#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


total_size = 0
status_codes = {}

if __name__ == "__main__":
    try:
        line_count = 0
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
                    print("File size:", total_size)
                    for code in sorted(status_codes):
                        print(f"{code}: {status_codes[code]}")
    except KeyboardInterrupt:
        print("File size:", total_size)
        for code in sorted(status_codes):
            print(f"{code}: {status_codes[code]}")
        sys.exit(0)
