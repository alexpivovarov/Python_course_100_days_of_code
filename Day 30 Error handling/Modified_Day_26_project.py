import pandas
data = pandas.read_csv("phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()} # formating data using dictionary comprehension
print(phonetic_dict)

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
