import random 
import time

def start_game():
    stage_count = 0
    is_game_finished = False

    input("\nPress enter when you are ready.")

    # Keep letting the user play until they finish the game
    while (not is_game_finished):
        is_game_finished = start_stage()
        stage_count += 1

    return stage_count

def get_substrings(six_letter_word, letter_count):
    substrings = []
    six_letter_word = six_letter_word.strip().lower()
    
    with open("words/filtered_words.txt", "r") as word_list:
        for word in word_list:
            word = word.strip().lower()
            
            if len(word) != letter_count:
                continue

            temp_letters = list(six_letter_word)
            can_form = True
            
            for letter in word:
                if letter in temp_letters:
                    temp_letters.remove(letter)  # remove one instance of the letter
                else:
                    can_form = False
                    break
            
            if can_form:
                substrings.append(word)
                
    return substrings


def start_stage():
    print("========== STAGE START ==========")

    # Get a random word (string) from the list of words 
    jumbled_word = random.choice(open('words/six_letter_words.txt').readlines())
    # Convert the string into a list of characters & remove the newline character
    jumbled_word = [ch for ch in jumbled_word if ch != '\n']
    # Shuffle items (letters) in the list (word)
    random.shuffle(jumbled_word)
    # Convert the list back into a string
    jumbled_word = ''.join(jumbled_word)

    substrings = [[]] * 4
    for i in range(3,-1,-1):
        # print(i)
        substrings[i] = get_substrings(jumbled_word, i + 3)

    print(substrings)

    print("Your jumbled word is: " + jumbled_word)
    for i in range(3,-1,-1):
        # print(i)
        print("The amount of " + str(i + 3) + " letter words is " + str(len(substrings[i])))
    print("You need to find the six-letter word to advance to the next stage.")
    input("Press Enter to continue.")

    words_found = []

    while (1):
        print("Time left: XXX")
        print("Words found: " + str(words_found))
        answer = input("Enter answer: ")
        if answer in substrings[0] or answer in substrings[1] or answer in substrings[2] or answer in substrings[3]:
            print("Word found! " + answer)
            words_found.append(answer)
        else:
            print("Answer not in the given words. Please try again.")

    return True