#!/usr/bin/python3

"""Reads from standard input and calculates metrics.
Computes statistics after every ten lines or a
keyboard interruption (CTRL + C).
Prints the total file size and the count of
read status codes up to that point.
"""


def print_metrics(file_size, status_counts):
    """Print accumulated metrics.

    Args:
        file_size (int): Accumulated size of the read file.
        status_counts (dict): Accumulated count of status codes.
    """
    print("Total file size: {}".format(file_size))
    for code, count in sorted(status_counts.items()):
        print("Status code {}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    file_size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_metrics(file_size, status_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                status = parts[-2]
                if status in valid_codes:
                    status_counts[status] = status_counts.get(status, 0) + 1
            except IndexError:
                pass

        print_metrics(file_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(file_size, status_counts)
        raise
