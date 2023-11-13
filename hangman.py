import random
import gspread
from google.oauth2.service_account import Credentials

class Hangman:
    def __init__(self):
        print("HANGMAN")
        print("Welcome to Hangman!")
        self.difficulty = self.select_difficulty()
        self.number_of_lives = self.get_number_of_lives(self.difficulty)
        self.chosen_word = self.get_word()

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

    def get_number_of_lives(self, difficulty):
        access_lives = {"Easy": 6, "Medium": 5, "Hard": 4}

        if difficulty == 1:
           easy_lives = access_lives["Easy"]
           print(f"You have {easy_lives} lives")
           return easy_lives
        elif difficulty == 2:
            medium_lives = access_lives["Medium"]
            print(f"You have {medium_lives} lives")
            return medium_lives
        elif difficulty == 3:
            hard_lives = access_lives["Hard"]
            print(f"You have {hard_lives} lives")
            return hard_lives

    def get_word(self):
        SCOPE = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]

        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open("hangman_words")
        WORDS = SHEET.worksheet('words')

        difficulty_column_words = WORDS.col_values(1)
        difficulty_column_words.pop(0)
        print(difficulty_column_words)