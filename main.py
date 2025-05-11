import game as game
import leaderboard as lb

print("WELCOME TO TEXT TWIST!\n\nMenu:\n[1] Start Game\n[2] View Leaderboard\n")

# Prompt user for choice input until the input is valid
while(1):
    user_choice = input("Enter your choice [1-2]: ")

    if (user_choice != '1' and user_choice != '2'):
        print("Invalid choice!")
        continue
    else:
        break

if (user_choice == '1'):
    print("You chose: Start Game")
    game.start_game()
elif (user_choice == '2'):
    print("You chose: View Leaderboard")
    lb.view_leaderboard()