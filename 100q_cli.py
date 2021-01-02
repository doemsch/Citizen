#!/usr/bin/python3

# This is the command line version of the 100 questions quiz. I plan coming up with some logic routines that will eventually be
# used for the GUI version.

from citizenlib import * # let's inport our parser so we can load our JSON
import sys

class citizen_proctor(object): # This is the class they'll be asking the questions!
    def __init__(self, json_to_load):
        self.json_to_load = json_to_load
        self.questions = {}

    def load_questions(self):
        tmp_obj = parse_questions()
        self.questions = tmp_obj.load_json(self.json_to_load)

    def __debug_print__(self):
        for k in self.questions.keys():
            print("Question: %s" % k)
            i = 65 # 'A' in ascii
            for a in self.questions[k].answers:
                print("\t%c: %s" % (chr(i), a))
                i += 1


def main(argv):
    x = citizen_proctor(argv[0])
    x.load_questions()
    x.__debug_print__()


# boiler plate to call main is our controlling function
if __name__ == '__main__':
    main(sys.argv[1:])

