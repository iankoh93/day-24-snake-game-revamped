# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAMES_PATH = r"./Input/Names/invited_names.txt"
LETTER_PATH = r"./Input/Letters/starting_letter.txt"
OUTPUT = r"./Output/ReadyToSend/"

with open(NAMES_PATH, "r") as file:
    raw_list = file.readlines()
    name_list = []
    for name in raw_list:
        name_list.append(name.strip())

for i in range(0, len(name_list)):
    with open(LETTER_PATH, mode="r") as file:
        old_letter = file.read()
        new_letter = old_letter.replace("[name]", f"{name_list[i]}")
        with open(OUTPUT + f"{name_list[i]}_letter.txt", mode="w") as newfile:
            newfile.write(new_letter)
