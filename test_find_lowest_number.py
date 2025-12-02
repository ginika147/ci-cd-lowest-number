# test_find_lowest_number.py
import subprocess
import os

def test_lowest_number_found(tmp_path):
    # Prepare input and output file paths
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"

    # Write test numbers to input file
    input_file.write_text("7\n3\n9\n5\n")

    # Run the script using subprocess
    result = subprocess.run(
        ["python", "find_lowest_number.py", str(input_file), str(output_file)],
        capture_output=True,
        text=True
    )

    # Read result from output file
    output = output_file.read_text().strip()

    # Assert the lowest number is correct
    assert output == "3.0"
