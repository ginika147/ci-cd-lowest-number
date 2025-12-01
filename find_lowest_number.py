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
                if not number_found:
                    lowest_number = num
                    number_found = True
                else:
                    if num < lowest_number:
                        lowest_number = num
            except ValueError:
                continue  # skip lines that aren't numbers

    if number_found:
        return lowest_number
    else:
        return "No numbers found in file"

if __name__ == '__main__':
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    result = find_lowest_number_in_file(input_filename)

    with open(output_filename, 'w') as output_file:
        output_file.write(str(result) + "\n")
