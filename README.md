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

## Features
### Existing Features
#### Introduction and Select Level of Difficulty:
The game title and levels of difficulty are the first things the user are presented with. The game title is coloured to make it stand out so the user is reminded of the game they are playing. Next, the user can pick the difficulty level they would like to play, or they can select random which will choose a random level for the user. The execution of each line is suspended for 1 second using the sleep() function to allow time for the user to read and to create flow instead of all text appearing at once.

![first-feature](assets/images/first-feature.png)


#### Number of Lives Section:
Once the user has chosen the level of difficulty they would like to play, the number of lives they have are revealed.
- Easy level: 6 lives
- Medium level: 5 lives
- Hard level: 4 lives

![second-feature](assets/images/second-feature.png)

#### Main Game Play Section
In this section, the terminal is cleared to make it clear that this is the main game section and to make the game less cluttered. The user is asked to input a letter they think could be in the word. If they make an incorrect guess, like in the example below, they will lose a life and the hangman image will reflect this by showing the first piece of the hangman

![fourth-feature](assets/images/fourth-feature.png)




