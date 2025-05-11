# words.txt from: https://github.com/dwyl/english-words 
# 5000-more-common.txt from: https://github.com/MichaelWehar/Public-Domain-Word-Lists
# This script filters the list of words in English to only include words that are 4-6 letters long.

word_list = open("words/words.txt", "r")

# Filter words of length 6       
# with open("words/six_letter_words.txt", "a") as six_letter_words:
#     for line in word_list:
#         if (len(line.strip()) == 6):            
#             six_letter_words.write(line.upper())

# Filter words of length 3-5
with open("words/filtered_words.txt", "a") as filtered_words:
    for line in word_list:
        if (len(line.strip()) >= 3 and len(line.strip()) < 6):            
            filtered_words.write(line.upper())