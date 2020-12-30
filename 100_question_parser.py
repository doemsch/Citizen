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

DEBUG = True # Gloabal variable called DEBUG set to "True"
WARNING = True

def debug(msg):                     # Debug function
    if DEBUG:                       # IF Debug is True
        print("DEBUG: %s" % msg)    #   print DEBUG: msg

def fatal(msg, exit_code):          # Fatal function
    print("FATAL: %s" % msg)                      # Print FATAL: msg
    exit(exit_code)                 # Exit with supplied error code

def warning(msg):                   # Warning message
    if WARNING:                     # IF Warning, print message
        print("WARNING: %s" % msg)  #   print WARNING: msg



class question(object): # This class will hold all the mechanics for a question
    def __init__(self, section, subsection, question): # we can create an object using question(section, subsection, question)
        self.question = question # take the question from the init function and store it in self.question
        self.section = section # ditto
        self.subsection = subsection # ditto
        self.answers = [] # an array of answers.



class parse_questions(object): # This class grinds through the text file and creates questions
    def __init__(self, question_file):      # create a parse_questions object and send in a question_file
        self.question_file = question_file  # store this in self.question_file
        self.question_data = []             # this will store the data inside self.question_file
        self.questions = {}                 # dictonary that will store instances of the object "question"

    
    def generate_csv(self, output_file):
        """
        This function generates a somewhat UGLY csv file
        """
        try:                                    # We are going to "try" something
            csv_file = open(output_file, 'w+')  # open "output_file" as a writable file and return a handle called "csv_file"
        except OSError as err:                  #   If something goes wrong with the open, we catch the exception
            fatal("{0}".format(err), -1)        # exit with something other than 0 so the shell knows something went wrong
        
        writer = csv.writer(csv_file)           # create a CSV writing object that's pointing at our open file handle

        writer.writerow(["Question","Answers"]) # Let's write the top row
        for k in self.questions.keys():         # Let's walk down the directory by key
            # write the "key" (which is the question) and then let's take the list of answers and create a comma delmited list.
            # this is likely totally wrong since you could have an answer in it that also has a comma...
            writer.writerow([k, ",".join(self.questions[k].answers)]) # insert a key (which is the question) and then let's take the array of 

        csv_file.close() # close the csv_file file handle
 

    def generate_json(self, output_file):
        """
        generate a json file that contains the contents of the self.questions structure using jsonpickle
        input self.questions
        output: output_file -> jsonpickle'd json document.
        """
        try:
            json_file = open(output_file, "w+")
        except OSError as err:
            fatal("generate_json {0}".format(err), -1)

        # create a frozen snapshot of the self.questions object and encode it into json
        frozen = jsonpickle.encode(self.questions)
        # write out the object
        json_file.write(frozen)
        # close the file
        json_file.close()

        

    def read_in_file(self):
        """
        This function reads in the file, but skips all the empty lines
        input: self.question_file
        output: self.quesiton_data
        """
        try:                                                                    # we are opening the file, this could fail..
            for line in open(self.question_file, 'r').readlines():              # Open the file and read in all the lines and put them in an array
                if line == '\n':                                                # if the line is simply equal to "\n"
                    continue                                                    # "continue" means "don't continue execution, go back to the top of the loop
                else:                                                           # the line simply isn't "\n" so let's append it.
                    self.question_data.append(line.rstrip())                             # append the line to the self.question_data array, strip the \n off
        except OSError as err:  # Let's capture the exception catch
            print("Problem opening question file: %s" % self.question_file)
            fatal("System Error {0}".format(err), -1) # let's print FATAL and the actual exception catch msg and exit -1
    
    
    def __debug_print__(self):
        """
        This function is here so we can look at the data I use the __debug as a pattern in my code.
        """
        print(self.question_data)

    def __debug_print_questions__(self):
        """
        Debug function to print out the contents of the self.questions dictonary
        """
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
        
        input: self.question_data
        output: self.questions dictionary loaded with question objectcs.
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
                subsection = line.split(":")[1] # split the line on the : into an array but only take the [1] element
                debug("Subsection: %s" % subsection)
            
            elif "." in line: # this is either a question or an answer?
                
                if line.split(".")[0].isdigit(): # case #3 it's a question, split on . into an array and take the element to the left and ask if it's a digit.
                    quest = line # Since we know it's something like "3. Are you a warlock?" we stick that in the quest varable.
                    debug("Question: %s" % quest)
                    # Create a question object and stick it in the dictonary with the key being the question (since we know it'll be unique)
                    self.questions[quest] = question(section, subsection, quest) # I know it's redundant to have the key and have a value.
                
                elif line.startswith("."): # case #4 answer All the answers startswith "." 
                    debug("Answer: %s" % line)
                    # take the question and append it to the answers array in the question object.
                    self.questions[quest].answers.append(line[2:]) # Trim the first two characters off the answer since it's ". the answer"
            
            else: # case #1 # This is section like AMERICAN DEMOCRACY
                section = line # load the line from the file into the section variable
                debug("Section = %s" % section)


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
