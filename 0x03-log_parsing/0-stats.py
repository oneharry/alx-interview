#!/usr/bin/python3
import sys
import re
import signal


pattern = r'^<(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})> - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\] "GET /projects/(\d+) HTTP/1\.1" (\d+) (\d+)$'

def status_code(x):
    return int(x[-2])

def print_lines(my_list):
    """Print statistics"""
    file_size = 0
    print("Total file size: {}".format(file_size))
    sorted_list = sorted(my_list, key=status_code)
    for line in sorted_list:
        split_line = line.split(' ')
        code = int(split_line[-2])
        print("status_code: {}".format(code))


def signal_handler(sig, frame):
    print_lines(line_list)
    sys.exit(0)

count = 0
line_list = []

for line in sys.stdin:
    res = re.findall(pattern, line)
    if res:
        continue
    else:
        line_list.append(line)
        if count == 9:
            print_lines(line_list)
            count = 0
        else:
            count += 1

signal.signal(signal.SIGINT, signal_handler)
