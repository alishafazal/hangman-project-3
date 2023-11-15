import random
import gspread
from google.oauth2.service_account import Credentials
from hangman_images import HangmanImages

class Hangman:

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self):
        print("HANGMAN\n")
        print("Welcome to Hangman!\n")
        self.difficulty = self.select_difficulty()
        self.number_of_lives = self.get_number_of_lives(self.difficulty)
        self.chosen_word = self.get_word(self.difficulty)
        self.current_word_hidden = self.get_hidden_word(self.chosen_word)
        self.hangman_images = self.get_hangman_images(self.difficulty)

    def select_difficulty(self):
        print("Which level of difficulty would you like to play?")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Random\n")

        valid_difficulty = False
        while valid_difficulty == False:
            try:
                user_selected_difficulty = int(input("Enter the number of the coressponding level(1-4):\n"))
                print()
                valid_difficulty = True
            except ValueError as e:
                print("Please enter a number between 1-4")
                continue

            if user_selected_difficulty == 1:
                print("You have selected to play game difficulty level: Easy\n")
            elif user_selected_difficulty == 2:
                print("You have selected to play game difficulty level: Medium\n")
            elif user_selected_difficulty == 3:
                print("You have selected to play game difficulty level: Hard\n")
            elif user_selected_difficulty == 4:
                print("You have selected to play game difficulty level: Random\n")
                user_selected_difficulty = random.randint(1, 3)
            else:
                print("Please enter a valid number\n")
                valid_difficulty = False

        return user_selected_difficulty

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

    def get_hangman_images(self, difficulty):
        if difficulty == 1:
            return HangmanImages.easy_lives_images()
        elif difficulty == 2:
            return HangmanImages.medium_lives_images()
        elif difficulty == 3:
            return HangmanImages.hard_lives_images()

    def make_a_guess(self):
        correct_input = False
        while correct_input == False:
            try:
                user_guess = input("Guess a letter:\n")
                if user_guess not in self.alphabet:
                    raise ValueError("Invalid input. Please enter a valid letter")
            except ValueError as e:
                print(f"ValueError: {e}")
            else:
                correct_input = True
        return user_guess

    def check_user_guess(self, user_guess, current_word_hidden):
        letter_match = False
        for index in range(len(self.chosen_word)):
            if self.chosen_word[index] == user_guess:
                current_word_hidden = current_word_hidden[:index] + user_guess + current_word_hidden[index + 1:]
                letter_match = True
        if letter_match == False:
            self.number_of_lives -= 1
        print(current_word_hidden)
        print(self.hangman_images[-(self.number_of_lives + 1)])
        print(f"You have {self.number_of_lives} lives remaining")
        return current_word_hidden

    def has_word_been_guessed(self, current_word_hidden):
        for letter in current_word_hidden:
            if letter == "-":
                return False
        return True

    def restart_game(self):
        valid_answer = False
        while valid_answer == False:
            play_again = input("Would you like to play again?\ny/n \n")
            if play_again == "y" or play_again == "n":
                valid_answer = True
            else:
                print("Please enter either y or n")
                valid_answer = False

        if play_again == "y":
            self.difficulty = self.select_difficulty()
            self.number_of_lives = self.get_number_of_lives(self.difficulty)
            self.chosen_word = self.get_word(self.difficulty)
            self.current_word_hidden = self.get_hidden_word(self.chosen_word)
            self.hangman_images = self.get_hangman_images(self.difficulty)
            self.run_game()


    def run_game(self):
        print("Let's play!\n")
        while self.number_of_lives > 0:
            user_guess = self.make_a_guess()
            self.current_word_hidden = self.check_user_guess(user_guess, self.current_word_hidden)
            word_guessed = self.has_word_been_guessed(self.current_word_hidden)
            if word_guessed == True:
                print("You won!")
                break
        if self.number_of_lives == 0:
            print("You lost:(")
        self.restart_game()