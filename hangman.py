"""
Imported packages and modules section
"""
import random  # used to generate random numbers
import time  # used to cause a delay in the excution of the code
import os  # used to clear the terminal
import gspread  # used to access data in the Google spreadsheet
from google.oauth2.service_account import Credentials
from hangman_images import HangmanImages
from termcolor import colored  # used to output coloured text


class Hangman:
    """
    The Hangman class contains all game variables and methods needed to
    play the game
    """
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
        ]

    def __init__(self):
        print(colored(("-------"), "yellow"))
        print(colored(("HANGMAN"), "cyan"))
        print(colored(("-------"), "yellow"))
        time.sleep(1)
        print("Welcome to Hangman!\n")
        time.sleep(1)
        self.difficulty = self.select_difficulty()
        self.number_of_lives = self.get_number_of_lives(self.difficulty)
        self.chosen_word = self.get_word(self.difficulty)
        self.current_word_hidden = self.get_hidden_word(self.chosen_word)
        self.hangman_images = self.get_hangman_images(self.difficulty)

    def select_difficulty(self):
        """
        User input corresponds to the level of difficulty the
        user would like to play at. Try except statement is nested
        within a while loop and checks if the user has entered an
        integer, if not, an error message will be raised. The loop is
        broken when valid input is entered
        """
        print("Which level of difficulty would you like to play?\n")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Random\n")
        time.sleep(1)

        valid_difficulty = False
        while valid_difficulty is False:
            try:
                user_selected_difficulty = int(input(
                    "Enter the number of the corresponding level(1-4):\n"))
                time.sleep(1)
                valid_difficulty = True
            except ValueError as e:
                print("Please enter a number between 1-4\n")
                continue

            if user_selected_difficulty == 1:
                print(
                    "\nYou have selected to play difficulty level: Easy\n")
                time.sleep(1)
            elif user_selected_difficulty == 2:
                print(
                    "\nYou have selected to play difficulty level: Medium\n")
                time.sleep(1)
            elif user_selected_difficulty == 3:
                print(
                    "\nYou have selected to play difficulty level: Hard\n")
                time.sleep(1)
            elif user_selected_difficulty == 4:
                print(
                    "\nYou have selected to play difficulty level: Random\n")
                time.sleep(1)
                user_selected_difficulty = random.randint(1, 3)
            else:
                print("\nPlease enter a valid number\n")
                valid_difficulty = False

        return user_selected_difficulty

    def get_number_of_lives(self, difficulty):
        """
        Accesses number of lives based on level of difficulty
        """
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
        """
        Code to use Google Sheets API to retrive the hangman words.
        if/elif statements access the easy, medium and hard words columns
        in the Google Sheet respectively, and returns a random word to
        use in the game.
        The code to access the spreadsheet data from lines 115-125 was
        inspired from Code Institute's "Love Sandwiches" walkthrough project
        """

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
        """
        For the random word, each letter of the random word
        is iterated over using a for loop, replaced with a
        dash and stored in a varible for use later in the game
        """
        hidden_word = ""
        hidden_letter = "-"
        for letter in chosen_word:
            hidden_word += hidden_letter
        return hidden_word

    def get_hangman_images(self, difficulty):
        """
        Gets the hangman images to use each time a life is lost, corresponding
        to the level of difficulty chosen
        """
        if difficulty == 1:
            return HangmanImages.easy_lives_images()
        elif difficulty == 2:
            return HangmanImages.medium_lives_images()
        elif difficulty == 3:
            return HangmanImages.hard_lives_images()

    def make_a_guess(self):
        """
        Try except else statement is placed within a while loop. If user
        input is not a letter of the alphabet, then a ValueError is raised.
        The loop is broken when valid input is entered. The user input is
        stored in a variable
        """
        correct_input = False
        while correct_input is False:
            try:
                user_guess = input("Guess a letter:\n")
                if user_guess not in self.alphabet:
                    raise ValueError(
                        "Invalid input. Please enter a valid letter")
            except ValueError as e:
                print(f"\nValueError: {e}\n")
            else:
                correct_input = True
        return user_guess

    def check_user_guess(self, user_guess, current_word_hidden):
        """
        Checks for a match between the user input and the letters
        within the chosen word. A dash is removed and replaced
        with correct input and for incorrect input a life
        is lost and the dashes will remain.
        The code on lines 199-200 was inspired from an article on
        Stack Overflow, as mentioned in the README file
        """
        letter_match = False
        for index in range(len(self.chosen_word)):
            if self.chosen_word[index] == user_guess:
                current_word_hidden = current_word_hidden[
                    :index] + user_guess + current_word_hidden[index + 1:]
                letter_match = True
        if letter_match is False:
            self.number_of_lives -= 1
        print(current_word_hidden)
        print(self.hangman_images[self.number_of_lives])
        print(f"You have {self.number_of_lives} lives remaining\n")
        return current_word_hidden

    def has_word_been_guessed(self, current_word_hidden):
        """
        For loop iterates over each letter in the current word to determine
        if any dashes remain which determines if the word has been guessed
        or not
        """
        for letter in current_word_hidden:
            if letter == "-":
                return False
        return True

    def restart_game(self):
        """
        Restarts the game if user inputs y, program stops if user inputs n.
        While loop checks whether the input is valid or not and is broken
        when valid input is given. When invalid input is given, the terminal
        will be cleared and an error message will display.
        The code on line 232 was inspired from fellow CI student Tucker, as
        mentioned in the README file.
        """
        valid_answer = False
        while valid_answer is False:
            play_again = input("Would you like to play again?\ny/n \n")
            os.system('cls||clear')
            if play_again == "y" or play_again == "n":
                valid_answer = True
            else:
                print(colored(("Please enter either y or n\n"), "yellow"))
                valid_answer = False

        if play_again == "y":
            self.difficulty = self.select_difficulty()
            self.number_of_lives = self.get_number_of_lives(self.difficulty)
            self.chosen_word = self.get_word(self.difficulty)
            self.current_word_hidden = self.get_hidden_word(self.chosen_word)
            self.hangman_images = self.get_hangman_images(self.difficulty)
            self.run_game()

    def run_game(self):
        """
        Runs the main game play. If statement is used to check whether
        the user has won or lost based on whether the word has been guessed
        or if there are no lives remaining
        The code on line 255 to clear the terminal was inspired from fellow
        CI student Tucker, as mentioned in the README file.
        """
        os.system('cls||clear')
        print("Let's play!\n")
        while self.number_of_lives > 0:
            user_guess = self.make_a_guess()
            self.current_word_hidden = self.check_user_guess(
                user_guess, self.current_word_hidden)
            word_guessed = self.has_word_been_guessed(self.current_word_hidden)
            if word_guessed is True:
                print(colored(("You won!:)\n"), "green"))
                break
        if self.number_of_lives == 0:
            print(colored(("You lost:(\n"), "red"))
        self.restart_game()
