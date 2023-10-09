student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


import pandas

student_data_frame = pandas.DataFrame(student_dict)




nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}




def generatae_phonetic():
    word_input = input("Enter a name?").upper()
    try:
        output_list = [nato_phonetic_dict[letter] for letter in word_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generatae_phonetic()
    else:
        print(output_list)


generatae_phonetic()