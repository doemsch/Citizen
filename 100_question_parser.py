#!/usr/bin/python3

# This program takes the text version of the 100 questions asked on the citizen test and parses them into a json document
#
# Howto Run program: 100_question_parser.py [input file] [csv output] [json output]
# example: 100_question_parser.py 100q.txt 100q.csv 100q.json
#
# TODO:
# [X] Add json output function
# [X] Adding detailed comments
# [ ] Add proper command line arguments
#
# just showing that I can edit! :-)

import jsonpickle # We are going to turn these questions into a big json document but because we are using classes, we'll just pickle it.
import sys, csv # We need sys for comand line

DEBUG = True
WARNING = True

# contains our classes and libraries
from citizenlib import *


def main(argv):
    x = parse_questions(argv[0])
    x.read_in_file()
    x.parse_question_data()
    #x.__debug_print__()
    #x.__debug_print_questions__()
    x.generate_csv(argv[1])
    x.generate_json(argv[2])

# Boiler plate
if __name__ == '__main__':
    main(sys.argv[1:])
