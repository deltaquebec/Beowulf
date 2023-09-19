import chardet

def delete_every_other_line(filename):
    # Detect the encoding of the text file
    with open(filename, "rb") as f:
        data = f.read()
        result = chardet.detect(data)
    with open(filename, 'r', encoding=result["encoding"]) as file:
        lines = file.readlines()

    with open(filename, 'w', encoding=result["encoding"]) as file:
        for i, line in enumerate(lines):
            if i % 2 == 1:
                file.write(line)

delete_every_other_line("00_slade.txt")
