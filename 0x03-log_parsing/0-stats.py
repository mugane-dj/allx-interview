#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == "__main__":
    ip_counts = {}
    total_size = 0
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    for status in status_codes:
        ip_counts[status] = 0
    line_counter = 0
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in ip_counts:
                ip_counts[status_code] += 1
            line_counter += 1
            if line_counter % 10 == 0:
                print("File size: {}".format(total_size))
                for status, count in ip_counts.items():
                    if count > 0:
                        print("{}: {}".format(status, count))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for status, count in ip_counts.items():
            if count > 0:
                print("{}: {}".format(status, count))
