import chardet

def split_file_into_10(input_file_name):
    # Open the input file and read its contents
    with open(input_file_name, "rb") as input_file:
        data = input_file.read()
        result = chardet.detect(data)

    with open(input_file_name, "r", encoding=result["encoding"]) as input_file:
        lines = input_file.readlines()

    # Compute the number of lines per output file
    num_lines_per_file = len(lines) // 10
    num_lines_last_file = len(lines) % 10

    # Create the output files
    for i in range(1, 11):
        # Determine the number of lines for this file
        if i == 10:
            num_lines = num_lines_per_file + num_lines_last_file
        else:
            num_lines = num_lines_per_file

        # Create the file name
        file_name = "{:02d}_oe.txt".format(i)

        # Open the output file and write the lines
        with open(file_name, "w", encoding=result["encoding"]) as output_file:
            start = (i - 1) * num_lines
            end = start + num_lines
            output_file.writelines(lines[start:end])

    # Print a message to indicate that the operation is complete
    print("Done")

split_file_into_10("00_oe.txt")
