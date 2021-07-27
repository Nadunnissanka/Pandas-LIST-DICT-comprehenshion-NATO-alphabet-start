import pandas

# TODO 1. Create a dictionary in this format:
dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def nato_converter():
    word = input("Enter a word that you wish to convert in to Nato format: ").upper()
    word_char_list = list(word)
    nato_alpha = [data_dict[letter] for letter in word_char_list]
    print(nato_alpha)


loop = True

while loop:
    try:
        nato_converter()
        loop = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
