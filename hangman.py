import random

class Hangman:
    def __init__(self):
        print("HANGMAN")
        print("Welcome to Hangman!")
        self.difficulty = self.select_difficulty()

    def select_difficulty(self):
        print("Which level of difficulty would you like to play?")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Random")

        valid_difficulty = False
        while valid_difficulty == False:
            user_selected_difficulty = int(input("Enter the number of the coressponding level:\n"))

            if user_selected_difficulty == 1:
                print("You have selected to play game difficulty level: Easy")
                valid_difficulty = True
            elif user_selected_difficulty == 2:
                print("You have selected to play game difficulty level: Medium")
                valid_difficulty = True
            elif user_selected_difficulty == 3:
                print("You have selected to play game difficulty level: Hard")
                valid_difficulty = True
            elif user_selected_difficulty == 4:
                print("You have selected to play game difficulty level: Random")
                user_selected_difficulty = random.randint(1, 3)
                valid_difficulty = True
            else:
                print("Please enter a valid number")
        
        return int(user_selected_difficulty)


            
            








     