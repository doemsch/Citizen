#!/usr/bin/env python3

# let's get started here!

# the overall goal is to create a quiz that asks me 20 randomly selected questions that are stored in a .csv file
# the answers are multiple choice (4) and there shall be one correct answer and three incorrect answers
# when i answer a question using the letters A-D, i shall get "Great job!" if correct or "More luck next time!" if incorrect
# after the twenty questions the score shall be displayed as a percentage
# i shall be able to exit out of the quiz by typing "X"

# i will outline my thoughts on how I envision this might happen in the sections below so that later i can work on them! :-)
# i will do some research as I go along...


# firstirst i need to be able to work with the data from the Excel spreadsheet

import csv

with open("D:/Doemsch/Python/citizen_q_and_a.csv","r") as citizen:
    this_file=citizen.read()
    print(this_file)


# any idea why this does not print the data from the Excel spreadsheet?
# actually it does


# okay, next step

# this could be helpful: https://larsesdohr.com/create-a-multiple-choice-test-from-an-excel-sheet-with-python-and-openpyxl/
# something like below should help me with choosing random questions

import random

print(random.randrange(1, 10)) 









