#!/usr/bin/env python
'''!
\package toolbox.generaltools
\brief General purpose tool kit

In this module are alle the tools of more or less 'general purpose' collected.

\date (c) 2021
\copyright GNU V3.0
\author Marcus Schwamberger, mambano
\email marcus@lederzeug.de
\version 0.1
'''
__version__ = "0.2"
__updated__ = "30.11.2021"
__author__ = "Marcus Schwamberger, mambano"

from math import trunc
import random as rd
import csv
import os



def dice(sides = 100, start = 1):
    """!
    This functions delivers a dice roll of a chosen one (as default d100).

    @param sides of the dice (upper limit for the random numbers)
    @param start lowest allowed value (usually 1) of random numbers
    @return a random number between [start, sides]
    """

    return rd.randint(start, sides)

def roll():
    """!
    This functions simulates a d100 roll with two d10 and delivers the result.

    @return a random numbers from 00 to 99.
    
    @todo the following has to be fully implemented
    - add logging?
    """
    tens = rd.randint(0,9) * 10
    ones = rd.randint(0,9)
    return tens+ones


def getIntOfNumber(number):
    """!
    This functions checks if its parameter is an instance of float or int and return its integer value. Floating point numbers will be truncated towards zero.
    Raises ValueError otherwise.

    @param number
    @raise ValueError if parameter is neither float nor int
    @return int value of the number. Floating point numbers will be truncated towards zero.
    """
    if (not isinstance(number,(float,int))):
        raise TypeError(f"Parameter is not a number - {type(number)} = {number}")
    elif isinstance(number, float):
        number = trunc(number)
    return number

# function to load all kinds of files open() can
def textFileReader(tablenumber:int, sourceFolder:str = "tables", fileExtension:str = ".csv"):
    """!
    This functions reads a file and returns the file content.
    By default a csv file will be loaded from table source folder, where each table is identified with its table number.

    @param tablenumber to load suitable csv filename, which contains that number. Leave blank if you do not want to load a table.
    @param sourceFolder where to finde the file
    @param fileExtension of the file to be loaded
    @return file content

    @todo the following has to be fully implemented
    - add logging
    - add json file name syntax
    - add reading base path from configuration
    """
    # initialize variable
    filename = ""
    
    # if tablenumber is an integer a table with that table number should be loaded. Apply filename syntax for it.
    if isinstance(tablenumber, int): filename = "tab_"+str(tablenumber)
    
    # open file and return it
    return open(os.path.join("./src/data",sourceFolder,filename+fileExtension), "r")

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
