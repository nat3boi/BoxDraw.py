#!/usr/bin/python3

import argparse

# Initialize the ArgumentParser
parser = argparse.ArgumentParser(
    prog='Box Drawer',
    description='Draws a box around string of text.'
)

# Define optional arguments
#
parser.add_argument(
    '-t', '--type', 
    default='r',
    choices=['r', 'rr', 'b', 'd'],
    #metavar='',
    help='[Regular, Regular(Rounded), Bold, Double]'
)
# Parse the arguments
args = parser.parse_args()

# Accessing the parsed arguments
if args.type == 'r':
    TL='┌'
    TR='┐'
    BL='└'
    BR='┘'
    HZ='─'
    VT='│'

elif args.type == 'rr':
    TL='╭'
    TR='╮'
    BL='╰'
    BR='╯'
    HZ='─'
    VT='│'

elif args.type == 'b':
    TL='┏'
    TR='┓'
    BL='┗'
    BR='┛'
    HZ='━'
    VT='┃'

else:
    STR=''
    TL='╔'
    TR='╗'
    BL='╚'
    BR='╝'
    HZ='═'
    VT='║'

USERIN = input('')

HZB = HZ * (len(USERIN) + 2)
TOP = TL + HZB + TR
MID = VT + ' ' + USERIN + ' ' + VT
BOT = BL + HZB + BR
 
print(TOP + '\n' + MID + '\n' + BOT)
