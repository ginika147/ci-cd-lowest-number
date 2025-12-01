# find_lowest_number.py
# StAuth10244: I Ginika Calistus Ezeh, 000932941 certify that this material is my original work.

import sys

def find_lowest_number_in_file(input_filename):
    number_found = False
    lowest_number = None

    with open(input_filename, 'r') as input_file:
        for line in input_file:
            try:
                num = float(line.strip())
                if not number_found or num < lowest_number:
                    lowest_number = num
                    number_found = True
            except ValueError:
                continue

    return lowest_number if number_found else "No numbers found in file"

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    result = find_lowest_number_in_file(input_filename)

    with open(output_filename, 'w') as output_file:
        output_file.write(str(result) + "\n" if isinstance(result, float) else result + "\n")
