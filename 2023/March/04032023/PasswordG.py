import random

comb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"


def passwordGenerator(n):
    return "".join(random.sample(comb, n))


length = int(input("Enter the lenght of the password: "))

print(passwordGenerator(length))


# Give me project ideas in python

# Path: DailyChallengeQuestions/2023/March/04032023/ProjectIdeas.py
import random

ideas = [
    "A simple calculator",
    "A simple game",
    "A simple chatbot",
    "A simple password generator",
    "A simple website",
    "A simple web app",
    "A simple desktop app",
]
