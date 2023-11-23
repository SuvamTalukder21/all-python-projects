# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open(file="Input/Names/invited_names.txt") as names:
#     n_list = names.readlines()
#     name_list = []
#     for name in n_list:
#         nam = name.strip("\n")
#         name_list.append(nam)
#
# # print(name_list)
#
# with open(file="Input/Letters/starting_letter.txt") as letter:
#     text = letter.read()
#     for names in name_list:
#         letter_for_names = text.replace("[name]", names)
#         with open(file=f"Output/ReadyToPrint/letter_for_{names}", mode="w") as letter_with_names:
#             letter_with_names.write(letter_for_names)


PLACEHOLDER = "[name]"


with open(file="./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open(file="./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(file=f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
