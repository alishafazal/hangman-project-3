# Hangman

The aim of this project was to create a fun and thought-provoking command-line based hangman game.

The user can select the difficulty level of the game, which is either easy, medium or hard. Once this is selected, the Google Sheets API retrieves a random word from the chosen difficulty words list in the Google spreadsheet. The chosen word is replaced with dashes to hide the word from the user. The user is then asked to input a letter, if the user guesses correctly, the dash is replaced with the letter. If they guess incorrectly, the user will lose a life. The user wins the game if they can guess the word before they run out of lives, if they cant they will lose. The user has a final option to play again or not.

![Am I responsive](assets/images/am-i-responsive.png)

## Table of contents
- [UX](#ux)
  - [Application Purpose](#application-purpose)
  - [Application Goals](#application-goals)
  - [Audience](#audience)
  - [Communication](#communication)

- [Design](#design)
  - [Wireframes](#wireframes)

- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)

- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [Solved Bugs](#solved-bugs)

- [Programs and Libraries Used](#programs-and-libraries-used)

- [Deployment](#deployment)

- [Credits](#credits)

## UX

### Application purpose
To allow users to be entertained and challenged through guessing an unknown word with a limited amount of guesses.

### Application goals
To expand users vocabulary and to provide a fun learning experience.

### Audience
As the game depicts an image of the hangman being hung when the game has been lost, the target audience is 15 years and over.

### Communication
- As the purpose of the game is to provide an entertaining yet challenging experience, I have intuitively designed the game so the user can easily work their way through the game from start to finish, with an option to restart the game at the end so their main focus is only guessing the word.
- As it is a command-line based game, I have added colour to certain words and sentances to provide a bit more excitement. All colours used have good contrast against the black background.

## Design
### Wireframes

Before I wrote any code, I planned the design of the game through the use of a flow chart as shown below, to help me visualise what I needed to build.

![Lucidchart](assets/images/lucid-chart.png)