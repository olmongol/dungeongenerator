#!/usr/bin/env python
'''!
\package toolbox.generaltools
\brief General purpose tool kit

In this module are alle the tools of more or less 'general purpose' collected.

\date (c) 2021
\copyright GNU V3.0
\author Marcus Schwamberger
\email marcus@lederzeug.de
\version 0.1
'''
__version__ = "0.1"
__updated__ = "12.11.2021"
__author__ = "Marcus Schwamberger"

import random as rd
import csv



def dice(sides = 100, start = 1):
    """!
    This functions delivers a dice roll of a chosen one (as default d100).

    @param sides of the dice (upper limit for the random numbers)
    @param start lowest allowed value (usually 1) of random numbers
    @return a random number between [start, sides]
    """

    return rd.randint(start, sides)



def readTable(filename = ""):
    """!
    This reads as table csv and creates a table dictionary from it:
    \dot table dictionary
    digraph {
        rankdir=LR
        ranksep=1
        nodesep=0.3
        node [shape=rect]

        WO2 [label="2nd column name/entry value"]
        WO1 [label="1st column name/entry value"]
        {rank=same
            PO [label="roll limit (int)"]
            dot1 [shape=point width=0]
            dot2 [shape=point width=0]
            dot3 [shape=point width=0]
            PO -> dot1 -> dot2 [arrowhead=none]
            dot2 -> dot3 [arrowhead=none,style=dotted]
        }
        dot1 -> WO1 [weight=20]
        dot2 -> WO2 [weight=20]
    }
    \enddot

    @param filename name of table csv to read
    @retval result dictionary with table structure
    """
    result = {}
    lines = []

    with open(filename, "r") as fp:
        for row in csv.reader(fp):
            lines.append(row)

    for row in range(1, len(lines)):
        result[lines[row][0].strip(' ')] = {}

        for col in range(1, len(lines[row])):
            result[lines[row][0].strip(' ')][lines[0][0]][col] = lines[row][col]

    return result



def list3int(ilist = []):
    """!
    This function tries to convert every list entry into an integer and sorts them.

    @ilist input list with numbers-as-string elements
    @retval result sorted list with integers

    """
    result = list(map(int, ilist))
    result = result.sort()
    return result
