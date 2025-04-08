input = input(" Enter your name here: ")

print(f"Your name in uppercase is {input.upper()}")
print(f"Your name in lowercase is {input.lower()}")
print(f"Total number of characters is {len(input.strip(" "))}")
print(f"Your name reversed: {input[::-1]}")