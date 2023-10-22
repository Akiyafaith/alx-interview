#!/usr/bin/python3
import sys
import signal


total_size = 0
status_codes = {}


# define the function to print the stats
def print_statistics():
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes):
        print(f"{status_code}: {status_codes[status_code]}")


# Handle the CRTL+C to print and exit
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


# set up a signal handler
signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    parts = line.strip().split()
    if len(parts) == 7:
        ip, _, _, status_code, file_size = parts[0], parts[5], int(parts[6])

        total_size += file_size

        if status_code in ['200', '301', '400',
                           '401', '403', '404', '405', '500']:
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        if len(status_codes) == 8 or total_size >= 10:
            print_statistics()
            total_size = 0
            status_codes = {}

print_statistics()
