import random 
import time

def start_game():
    stage_count = 0
    score_time = 0
    is_game_finished = False

    input("\nPress enter when you are ready.")

    # Keep letting the user play until they finish the game
    while (not is_game_finished):
        stage_details = start_stage(stage_count)
        print(stage_details)
        is_game_finished = stage_details[0]
        score_time = stage_details[1]
        stage_count += 1

    return stage_count, score_time

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


def start_stage(stages_completed):
    print("\n========== STAGE START ==========")

    # Get a random word (string) from the list of words 
    six_letter_word = random.choice(open('words/six_letter_words.txt').readlines())
    # Convert the string into a list of characters & remove the newline character
    jumbled_word = [ch for ch in six_letter_word if ch != '\n']
    # Shuffle items (letters) in the list (word)
    random.shuffle(jumbled_word)
    # Convert the list back into a string
    jumbled_word = ''.join(jumbled_word)

    substrings = [[]] * 4
    for i in range(3,-1,-1):
        # print(i)
        substrings[i] = get_substrings(jumbled_word, i + 3)

    # print(substrings)
    print(six_letter_word)

    print("Your jumbled word is: " + jumbled_word)
    for i in range(3,-1,-1):
        # print(i)
        print("The amount of " + str(i + 3) + " letter words is " + str(len(substrings[i])))
    print("You need to find the six-letter word to advance to the next stage.")
    input("Press Enter to continue.")

    additional_time = 0
    start_time = time.time()
    end_time = start_time + 30 + additional_time
    time_left = 120
    words_found = []

    while (time_left > 0):
        time_left = end_time - time.time()
        print("\nYour jumbled word is: " + jumbled_word)
        print("Time left: " + str(int(time_left)) + " seconds")
        print("Words found: " + str(words_found))
        answer = input("Enter answer: ")

        if answer == six_letter_word.strip().lower():
            time_taken = time.time() - start_time
            print("The word has been found in " + str(int(time_taken)) + " seconds. Onto the next level!")
            additional_time = end_time - time_taken
            return False if stages_completed < 3 else True, int(time_taken)

        elif answer in substrings[0] or answer in substrings[1] or answer in substrings[2] or answer in substrings[3]:
            print("Word found! " + answer)
            words_found.append(answer)

        else:
            print("Answer not in the given words. Please try again.")

    return True, 0