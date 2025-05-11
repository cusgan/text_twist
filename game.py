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

def start_stage():
    print("========== STAGE START ==========")

    jumbled_word = random.choice(open('words/six_letter_words.txt').readlines())
    # jumbled_word = random.shuffle(jumbled_word)
    print("Your jumbled word is: " + jumbled_word)
    return True