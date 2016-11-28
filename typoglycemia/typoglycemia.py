#
# Typoglycemia
#
# Scramble the letters of words in a string so that the first
# and last letters remain the same, but middle letters are 
# rearranged. Don't let words remain unchanged unless they are
# too short to change.
#


#
# 2016-11-14
#

import random
import sys
import re


def shuffle_word(word):
    'Randomly rearrange the middle letters of a word.'
    #word=sys.argv[1]
    if(len(word) > 3):
        middle_list = list(word[1:-1])
        middle = ''
        while(middle=='' or middle==word[1:-1]):
            # do this in a loop so we can make sure the output is different
            random.shuffle(middle_list)
            middle = ''.join(middle_list)
        return(word[0] + middle + word[-1])
    else:
        return(word)


def gibberish(mystr):
    'Rearrange the middle letters in all words of a string.'
    #mystr = sys.argv[1]
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


gibberish(sys.argv[1])
