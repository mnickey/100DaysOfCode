# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas

alpha_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row.letter:row.code for (index, row) in alpha_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter your name: ").upper()

result = [my_dict[letter] for letter in user_input if letter.isalpha()]
print(result)
#
# for letter in user_input:
#     if not letter.isalpha():
#         print(" ")
#         continue
#     print(my_dict[letter])
