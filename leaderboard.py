def view_leaderboard():
   leaderboard = open("leaderboard.txt", "r")

   print("\n========== LEADERBOARD ==========")
   print("Rank\tName\t\tTime\tHighest Stage Completed")

def add_to_leaderboard(time, stages_completed):
   user_name = input("Enter your name: ")

   with open("leaderboard.txt", "a") as leaderboard:
      leaderboard.write(user_name + "," + str(time) + "," + str(stages_completed) + "\n")