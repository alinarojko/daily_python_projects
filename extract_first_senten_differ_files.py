from pathlib import Path

filepathes = Path("files").glob("*.txt")

for file in filepathes:
    with open(file, "r") as infile:
        content = infile.read().split(".")[0] + "\n"
    print(content)