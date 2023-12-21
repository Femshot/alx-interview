#!/usr/bin/python3
""" Log parsing script that reads from stdin and computes metrics based on
certain conditions"""


file_size = 0
codes = {}
ref_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
if __name__ == "__main__":
    import sys

    try:
        for line in sys.stdin:
            words = line.split()
            if len(words) == 9 and '/projects/260' in words:
                file_size += int(words[-1])
                if words[-2] in ref_codes:
                    codes[words[-2]] = codes.get(words[-2], 0) + 1
                count += 1
            if count == 10:
                print(f"File size: {file_size}")
                for code in sorted(codes.keys()):
                    print(f"{code}: {codes[code]}")
                count = 0
    except KeyboardInterrupt as err:
        print(f"File size: {file_size}")
        for code in sorted(codes.keys()):
            print(f"{code}: {codes[code]}")
        raise err
