Python Programming Tasks
This repository contains four Python programming tasks completed as part of the CodeAlpha internship program.
Tasks Overview
Task 1: Hangman Game
A classic word guessing game where players try to guess a hidden word letter by letter.
Features:
·	Random word selection from a predefined list
·	Letter validation and duplicate checking
·	Wrong guess tracking with maximum attempts
·	Win/lose conditions
How to run:
python task1.py

Task 2: Stock Portfolio Tracker
A simple application to track stock investments and calculate portfolio value.
Features:
·	Predefined stock prices for popular companies
·	Add multiple shares of different stocks
·	Calculate total portfolio value
·	Save portfolio summary to text file
How to run:
python task2.py

Task 3: Task Automation Scripts
A collection of automation tools for common file and web tasks.
Features:
·	Move .jpg files between folders
·	Extract email addresses from text files
·	Scrape webpage titles and save to file
·	Interactive menu system
Requirements:
pip install requests

How to run:
python task3.py

Task 4: Basic Chatbot
A simple conversational chatbot that responds to various user inputs.
Features:
·	Greeting and farewell responses
·	Basic conversation patterns
·	Joke telling capability
·	Time and weather responses
·	Default responses for unknown inputs
How to run:
python task4.py

File Structure
python_programming_tasks/
├── task1.py          # Hangman Game
├── task2.py          # Stock Portfolio Tracker
├── task3.py          # Task Automation Scripts
├── task4.py          # Basic Chatbot
└── README.md         # This file

Requirements
·	Python 3.6 or higher
·	requests library (for Task 3 only)
Installation
1.	Clone or download this repository
2.	Install required dependencies:
3.	pip install requests

4.	Run any task using Python:
5.	python taskX.py

Usage Examples
Task 1 - Hangman
Welcome to Hangman!
Guess the word letter by letter
The word has 6 letters

Word: _ _ _ _ _ _
Wrong guesses: 0/6
Guessed letters: 
Enter a letter: p
Good! 'p' is in the word!

Task 2 - Stock Portfolio
=== Stock Portfolio Tracker ===
Available stocks:
  AAPL: $180.5
  TSLA: $250.75
  GOOGL: $140.25

Enter stock symbol (or 'done' to finish): AAPL
How many shares of AAPL? 10
Added 10 shares of AAPL

Task 3 - Automation
=== Task Automation Script ===
1. Move .jpg files
2. Extract emails from text file
3. Scrape webpage title
4. Exit

Choose an option (1-4): 1

Task 4 - Chatbot
=== Simple Chatbot ===
Hello! I'm a basic chatbot. Type 'bye' to exit.

You: Hello
Bot: Hi there! What's on your mind?

You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything!

Notes
·	All tasks include basic error handling
·	Files created by the programs will be saved in the same directory
·	Task 3 requires internet connection for webpage scraping
·	The chatbot uses simple pattern matching for responses
Author
Created as part of CodeAlpha Python Programming Internship
