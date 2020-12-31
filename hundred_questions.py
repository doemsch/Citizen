#!/usr/bin/env python3

# Let's get started here!

# the overall goal is to create a quiz that asks me 20 randomly selected questions that are stored in a .csv file
# the answers are multiple choice (4) and there shall be one correct answer and three incorrect answers
# when I answer a question using the letters A-D, I shall get "Great job!" if correct or "More luck next time!" if incorrect
# after the twenty questions the score shall be displayed as a percentage
# I shall be able to exit out of the quiz by typing "X"

# I will outline my thoughts on how I envision this might happen in the sections below so that later I can work on them! :-)
# I will do some research as I go along...


# First I need to be able to work with the data from the Excel spreadsheet

import csv

with open("D:/Doemsch/Python/citizen_q_and_a.csv","r") as citizen:
    this_file=citizen.read()
    print(this_file)


# Any idea why this does not print the data from the Excel spreadsheet?











