#!/usr/bin/env python3

# create a citizen q&a test

#let's add the needed tools to start with

import csv
import random


#now let's open the needed document

with open("D:/Doemsch/Python/citizen_q_and_a.csv","r") as citizen:
    this_file=citizen.read()


# retrieving a random question number from the file

for number in Question_Number:
    number = random(range(20))
print(number)


# hm, problem here, i want to print the questions... not the question numbers
# let me worry about that later
# actually, let's try this instead

for questions in Question:
    random.choice(questions)
print(questions)


# now the answers...
# found this random.shuffle... hopefully that works...

for answers in Answer:
    random.shuffle(answers)
print(answers)


# now how to give responses...
# need to be able to give capitalized letters to each answer so that the user can answer with a single letter
# maybe by making changes to the print line...

print("A", answers)


# this may work for one answer... but not for four of them...
# okay for now let's move on and look at how to get a response and give feedback if it is correct or not
# need to add that exist part...

print("What do you reckon is the correct answer? Please answer with A, B, C, or D. If you can't be bothered anymore, type X to exist this amazing quiz!")
response = str(input)

def testing(response):
    correct = Value TRUE
    if response correct:
        print("Rock Star!")
    else:
        print("Okay, you gave it a shot that shot did not win you the championship or the citizenship in fact!")

testing(response)


# let's talk about the overall score
# after the whole 20 questions, print a summary
# i am fairly certain this doesn't work, but it might be a start...

score = sum(TRUE)   
print(score)







































