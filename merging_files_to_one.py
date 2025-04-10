import pandas as pd
import csv


from pathlib import Path
# To create the list of filepathes
filepathes = Path("files").glob("*.txt")

# Create new file
with open("new_file.txt", "w") as outfile:
    # Iterate for each file in the list of filepathes
    for item in filepathes:
        # Open each file and extract data
        with open(item, "r") as infile:
            content = infile.read()
            outfile.write(content)




