#!/usr/bin/python3
"""
Log parsing script that computes metrics from stdin input.
"""

import sys
from collections import defaultdict


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
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
