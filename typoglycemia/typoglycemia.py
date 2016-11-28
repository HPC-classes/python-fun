#
# Typoglycemia
#
# Scramble the letters of words in a string so that the first
# and last letters remain the same, but middle letters are 
# rearranged. Don't let words remain unchanged unless they are
# too short to change.
#

#
# This example uses slices, lists, sets, loops, conditional 
# statements, function definitions, command line arguments, 
# and a simple regular expression.
#
# It takes a multi-word string as a command line argument.
#     e.g:   python typoglycemia.py "Remains to be seen if glass caskets become popular"
#

import random
import sys
import re


def shuffle_word(word):
    'Randomly rearrange the middle letters of a word.'
    if(len(word) < 4):
        # Can't rearrange words with less than 4 letters
        return(word)
    middle_list = list(word[1:-1])
    num_unique_chars = len(set(middle_list)) # python sets only contain unique elements
    if(num_unique_chars == 1):
        # Can't rearrange words where the middle letters are identical (e.g. "look")
        return(word)
    middle = ''
    while(middle=='' or middle==word[1:-1]):
        # do this in a loop so we can make sure the output is different
        random.shuffle(middle_list)
        middle = ''.join(middle_list)
    return(word[0] + middle + word[-1])


def parse_string(mystr):
    'Rearrange the middle letters in all words of a string.'
    mylist = list(mystr)
    newstr=''
    tempstr=''
    for ch in mylist:
        if re.match('[A-Za-z]', ch):
            tempstr += ch
        else:
            newstr += shuffle_word(tempstr)
            newstr += ch
            tempstr = ''
    newstr += shuffle_word(tempstr)
    print(newstr)


parse_string(sys.argv[1])
