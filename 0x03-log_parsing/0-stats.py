#!/usr/bin/env python3
import sys
import signal
import re


total_size = 0
line_count = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
status_codes_set = set(status_codes.keys())

log_pattern = re.compile(
    r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)


def print_statistics():
    """Print accumulated statistics."""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption to print statistics and exit."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)
    if match:
        status_code, file_size = match.groups()
        file_size = int(file_size)
        total_size += file_size
        if status_code in status_codes_set:
            status_codes[status_code] += 1
    line_count += 1
    if line_count % 10 == 0:
        print_statistics()
