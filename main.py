# TODO: Create a letter using starting_letter.txt
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as data:
    names = data.readlines()



with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as base_letter:
    letters = base_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace("[name]", stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)

















# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
