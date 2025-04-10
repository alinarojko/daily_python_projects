import pandas as pd
import csv
from pathlib import Path

filepathes = Path("files").glob("*.txt")

with open("new_file.txt", "w") as outfile:
    for item in filepathes:
        with open(item, "r") as infile:
            content = infile.read()
            outfile.write(content)




