import pandas
data = pandas.read_csv("phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} # formating data using dictionary comprehension
print(phonetic_dict)

user_word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_word]
print(output_list)
