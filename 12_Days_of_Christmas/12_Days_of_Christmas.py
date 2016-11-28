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
# The output of your script should look like this:
# (Provide printed example of the full song).
#

lines = [
    'On the %s day of Christmas my true love gave to me:',
    'A Partridge in a Pear Tree',
    'Two Turtle Doves',
    'Three French Hens',
    'Four Calling Birds',
    'Five Golden Rings',
    'Six Geese a-Laying',
    'Seven Swans a-Swimming',
    'Eight Maids a-Milking',
    'Nine Ladies Dancing',
    'Ten Lords a-Leaping',
    'Eleven Pipers Piping',
    'Twelve Drummers Drumming'
]



lines2 = [
    ['','','On the %s day of Christmas my true love gave to me:'],
    ['A','First','Partridge in a Pear Tree'],
    ['Two','Second','Turtle Doves'],
    ['Three','Third','French Hens'],
    ['Four','Fourth','Calling Birds'],
    ['Five','Fifth','Golden Rings'],
    ['Six','Sixth','Geese a-Laying'],
    ['Seven','Seventh','Swans a-Swimming'],
    ['Eight','Eighth','Maids a-Milking'],
    ['Nine','Ninth','Ladies Dancing'],
    ['Ten','Tenth','Lords a-Leaping'],
    ['Eleven','Eleventh','Pipers Piping'],
    ['Twelve','Twelfth','Drummers Drumming']
]

lines3 = [
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
    print(lines3[0][1] % lines3[day][0])
    for line in range(day,0,-1):
        if(line == 1 and day > 1):
            print('And ' + lines3[line][1])
        else:
            print(lines3[line][1])
    print('')



