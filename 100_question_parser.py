#!/usr/bin/python3

# This program takes the text version of the 100 questions asked on the citizen test and parses them into a json document
#
# Howto Run program: 100_question_parser.py 100q.txt
# output's files 
#
#
# TODO:
# Add json output function
# 
# just showing that I can edit! :-)

import json # We are going to turn these questions into a big json document.
import sys, csv

class question(object): # This class will hold all the mechanics for a question
    def __init__(self, section, subsection, question):
        self.question = question
        self.section = section
        self.subsection = subsection
        self.answers = []

DEBUG = True

def debug(msg):
    if DEBUG: 
        print("DEBUG: %s" % msg)


class parse_questions(object): # This class grinds through the text file and creates questions
    def __init__(self, question_file):
        self.question_file = question_file
        self.question_data = []
        self.questions = {}

    
    def generate_csv(self, output_file):
        """
        This function generates a somewhat UGLY csv file
        """
        try:
            csv_file = open(output_file, 'w+')
        except OSError:
            debug("Unable to write CSV file: %s" % output_file)
            exit(-1)
        
        writer = csv.writer(csv_file)

        writer.writerow(["Question","Answers"])
        for k in sorted(self.questions.keys()):
            writer.writerow([k, ",".join(self.questions[k].answers)])

        csv_file.close()

    def generate_json(self, output_file):
        """
        generate a json file
        """
        try:
            json_file = open(output_file, "w+")
        except OSError:
            debug("Unable to open JSON file for output!!")
            exit(-1)

        json.dump(self.questions.__dict__, json_file)

        json_file.close()

        

    def read_in_file(self):
        """
        This function reads in the file, but skips all the empty lines
        """
        try:
            for line in open(self.question_file, 'r').readlines():              # Open the file and read in all the lines
                if line == '\n':                                                # if the line is simply equal to "\n"
                    continue                                                    # "continue" means "don't continue execution, go back to the top of the loop
                else:
                    self.question_data.append(line.rstrip())                             # append the line to the self.question_data array, strip the \n off
        except:
            print("Problem opening question file: %s" % self.question_file)
            exit(-1) # let's bail out.. if we can't open the file why are we here?
    
    
    def __debug_print__(self):
        """
        This function is here so we can look at the data I use the __debug as a pattern in my code.
        """
        print(self.question_data)

    def __debug_print_questions__(self):
        for k in sorted(self.questions.keys()):
            print("Question: %s" %k)
            for a in self.questions[k].answers:
                print("\t%s" % a)

    
    def parse_question_data(self):
        """ 
        This function walks through the question data and digs out the questions
        if a line starts with "_:" it's either a subsection or a question.
        if a line starts with a "." it's an answer
        if it starts with neither of those it's a secion
        """
        section = ''
        subsection = ''
        quest = ''
        # The data falls into 4 cases
        # 1. Sections
        # 2. subsections
        # 3. questions
        # 4. answers.

        for line in self.question_data:

            if ":" in line: # case #2
                subsection = line.split(":")[1]
                debug("Subsection: %s" % subsection)
            
            elif "." in line: # this is either a question or an answer?
                
                if line.split(".")[0].isdigit(): # case #3 it's a question
                    quest = line
                    debug("Question: %s" % quest)
                    self.questions[quest] = question(section, subsection, quest) # I know it's redundant to have the key and have a value.
                
                elif line.startswith("."): # case #4 answer 
                    debug("Answer: %s" % line)
                    self.questions[quest].answers.append(line[2:]) # Trim the first two characters off the answer since it's ". the answer"
            
            else: # case #1
                section = line
                debug("Section = %s" % section)


def main(argv):
    x = parse_questions(argv[0])
    x.read_in_file()
    x.parse_question_data()
    #x.__debug_print__()
    x.__debug_print_questions__()
    x.generate_csv(argv[1])
    x.generate_json(argv[2])

if __name__ == '__main__':
    main(sys.argv[1:])
