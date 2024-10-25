#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print accumulated statistics
    Args:
        total_size: Total file size
        status_codes: Dictionary of status codes and their counts
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def extract_input(input_line):
    """
    Extract relevant information from a log line using regex
    Returns:
        Tuple of (status_code, file_size) or None if line is invalid
    """
    log_format = (
        r'\S+ - \[.+\] "GET /projects/260 HTTP/1.1" '
        r'([0-9]{3}) ([0-9]+)'
    )
    match = re.match(log_format, input_line)

    if match:
        status_code = match.group(1)
        file_size = int(match.group(2))
        return (status_code, file_size)
    return None


def main():
    """Main function to process log input"""
    total_size = 0
    line_count = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            result = extract_input(line)

            if result:
                status_code, file_size = result
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
