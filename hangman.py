import random
import gspread
from google.oauth2.service_account import Credentials

class Hangman:

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self):
        print("HANGMAN\n")
        print("Welcome to Hangman!\n")
        self.difficulty = self.select_difficulty()
        self.number_of_lives = self.get_number_of_lives(self.difficulty)
        self.chosen_word = self.get_word(self.difficulty)
        self.current_word_hidden = self.get_hidden_word(self.chosen_word)

    def select_difficulty(self):
        print("Which level of difficulty would you like to play?")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Random\n")

        valid_difficulty = False
        while valid_difficulty == False:
            user_selected_difficulty = int(input("Enter the number of the coressponding level:\n"))
            print()

            if user_selected_difficulty == 1:
                print("You have selected to play game difficulty level: Easy\n")
                valid_difficulty = True
            elif user_selected_difficulty == 2:
                print("You have selected to play game difficulty level: Medium\n")
                valid_difficulty = True
            elif user_selected_difficulty == 3:
                print("You have selected to play game difficulty level: Hard\n")
                valid_difficulty = True
            elif user_selected_difficulty == 4:
                print("You have selected to play game difficulty level: Random\n")
                user_selected_difficulty = random.randint(1, 3)
                valid_difficulty = True
            else:
                print("Please enter a valid number\n")
        
        return int(user_selected_difficulty)

    def get_number_of_lives(self, difficulty):
        access_lives = {"Easy": 6, "Medium": 5, "Hard": 4}

        if difficulty == 1:
           easy_lives = access_lives["Easy"]
           print(f"You have {easy_lives} lives\n")
           return easy_lives
        elif difficulty == 2:
            medium_lives = access_lives["Medium"]
            print(f"You have {medium_lives} lives\n")
            return medium_lives
        elif difficulty == 3:
            hard_lives = access_lives["Hard"]
            print(f"You have {hard_lives} lives\n")
            return hard_lives

    def get_word(self, difficulty):
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

        if difficulty == 1:
            easy_column_words = WORDS.col_values(1)
            easy_column_words.pop(0)
            easy_random_word = random.choice(easy_column_words)
            return easy_random_word
        elif difficulty == 2:
            medium_column_words = WORDS.col_values(2)
            medium_column_words.pop(0)
            medium_random_word = random.choice(medium_column_words)
            return medium_random_word
        elif difficulty == 3:
            hard_column_words = WORDS.col_values(3)
            hard_column_words.pop(0)
            hard_random_word = random.choice(hard_column_words)
            return hard_random_word

    def get_hidden_word(self, chosen_word):
        hidden_word = ""
        hidden_letter = "-"
        for letter in chosen_word:
            hidden_word += hidden_letter
        return hidden_word

    def make_a_guess(self):
        correct_input = False
        while correct_input == False:
            try:
                user_guess = input("Guess a letter:\n")
                if user_guess not in self.alphabet:
                    raise ValueError("You entered an invalid input. Please enter a valid letter")
            except ValueError as e:
                print(f"ValueError: {e}")
            return user_guess     

    def run_game(self):
        print("Let's play!\n")
        user_guess = self.make_a_guess()


    

    