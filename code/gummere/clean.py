import os
import re
import chardet

# Directory where the text files are located
directory = r"C:\Users\delta\AppData\Local\Programs\Python\Python37\hw\project\gummere"

# Go through all files in the directory
for filename in os.listdir(directory):
    # Only process files that end with ".txt"
    if filename.endswith(".txt"):
        # Detect the encoding of the text file
        with open(os.path.join(directory, filename), "rb") as f:
            data = f.read()
            result = chardet.detect(data)

        # Open the file and read its contents
        with open(os.path.join(directory, filename), "r", encoding=result["encoding"]) as file:
            text = file.read()

        # Remove all numbers from the text using a regular expression
        text = re.sub(r'\d+', '', text)

        # Remove all left and right brackets
        text = text.replace('[','').replace(']','').replace('(','').replace(')','')

        # Remove all vertical whitespace using a regular expression
        text = re.sub(r'\n\s*\n', '\n', text)

        # Remove spaces between words if there is more than one space, except at the end of lines
        text = re.sub(r'(?<!\n)\s{2,}(?!\n)', ' ', text)

        # Remove all Roman Numerals if they are the only items on their respective lines
        text = re.sub(r'^[IVXLCDM]+$[\r\n]+', '', text, flags=re.MULTILINE)

        # Left justify the text
        text = text.lstrip()

        num_lines = sum(1 for line in text)

        # Save the processed text back to the file
        with open(os.path.join(directory, filename), "w", encoding=result["encoding"]) as file:
            file.write(text)

        print(f"The file contains {num_lines} lines.")
