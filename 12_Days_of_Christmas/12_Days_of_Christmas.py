#
# The Twelve Days of Christmas
#
# Write a python script that prints the full song "The
# Twelve Days of Christmas".
# 
# Each line of the song may appear only once in your code.
#
# Note that on the first day, there is no "and" before "a
# partridge in a pear tree".
#

#
# This example uses a two-dimensional array/list, for loops,
# conditional statements, and the string format operator (%).
#

lines = [
    ['','On the %s day of Christmas,\nMy true love gave to me:'],
    ['First','A Partridge in a Pear Tree.'],
    ['Second','Two Turtle Doves,'],
    ['Third','Three French Hens,'],
    ['Fourth','Four Calling Birds,'],
    ['Fifth','Five Golden Rings,'],
    ['Sixth','Six Geese a-Laying,'],
    ['Seventh','Seven Swans a-Swimming,'],
    ['Eighth','Eight Maids a-Milking,'],
    ['Ninth','Nine Ladies Dancing,'],
    ['Tenth','Ten Lords a-Leaping,'],
    ['Eleventh','Eleven Pipers Piping,'],
    ['Twelfth','Twelve Drummers Drumming,']
]

for day in range(1,13):
    print(lines[0][1] % lines[day][0])
    for line in range(day,0,-1):
        if(line == 1 and day > 1):
            print('And ' + lines[line][1])
        else:
            print(lines[line][1])
    print('')



