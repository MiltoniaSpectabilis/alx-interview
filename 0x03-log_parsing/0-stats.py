#!/usr/bin/python3
"""
Log parsing script that computes metrics from stdin input.
"""

import sys


def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """Parse a single line of log input."""
    try:
        parts = line.split()
        return int(parts[-2]), int(parts[-1])
    except (ValueError, IndexError):
        return None, None


def main():
    """Main function to process log input and compute metrics."""
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
