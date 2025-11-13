PLACEHOLDER = "[name]"
list_of_names = []

with open("./Input/Names/invited_names.txt", "r") as f:
    names = (f.readlines())

for name in names:
    name = name.strip('\n')
    list_of_names.append(name)

with open("./Input/Letters/starting_letter.txt", "r") as message_file:
    starting_letter = message_file.read()
    for name in list_of_names:
        personalized_letter = starting_letter.replace(PLACEHOLDER, name)
        output_filename = f"./Output/ReadyToSend/letter_for_{name}.txt"
        with open(output_filename, mode="w") as output_file:
            output_file.write(personalized_letter)
