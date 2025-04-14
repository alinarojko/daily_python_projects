import csv
import os

# Create variable to check if file exist , and apply check for size
filename = "vocabulary.csv"
file_exist = os.path.isfile(filename) and os.path.getsize(filename) > 0

# Create empty list , we can't use te array , it doesn't have keys
data = {}

# Check if file is not here , we create new file , in append method , to add new data  to it
if not file_exist:
    with open("vocabulary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Language 1", "Language 2"])

# collect new words from the input , convert to lower
while True:
    word = input(" Enter a word in Language 1 , (or type 'done' to finish) : ")
    if word.lower() == "done":
        print("Exiting the program and saving!")
        break

    if not word:
        print("Please enter a word!")
        continue

    translation = input(f" Enter a translation of the {word} "
                            f"in Language 2: " )
    if not translation:
        print("Please enter translation!")
        continue

# add translation value to key "word"
    data[word] = translation

# Open file in append mode add new inputs
    with open("vocabulary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([word.strip(), translation.strip()])


print("Your Bilingual Vocabulary list: ")
for word, translation in data.items():
    with open("vocabulary.csv", "r") as file:
        content = csv.reader(file)
        # Check each row and print it out
        for row in content:
            print(f"{row[0]} (Language 1): {row[1]} (Language 2)")


