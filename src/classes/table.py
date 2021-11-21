from classes.tablerollresult import TableRollResult
from toolbox.generaltools import textFileReader, getIntOfNumber
from math import trunc
import csv

class Table():
    """!
    This Class handles reading a table from file and provides several operations for it.
    """
    def __init__(self, tablenumber:int = 100) -> None:
        """!
        Constructor which loads a table with the given table number.

        @param a number. Floating point numbers will be truncated towards zero.
        """
        # check parameter is a number and receive its int value
        tablenumber = getIntOfNumber(tablenumber)

        # initialize variables
        self._table = {}
        lines = []

        # read csv file and put each line in a list
        for line in csv.reader(textFileReader(tablenumber)):
            lines.append(line)

        # assume that first line in each csv file contains header names only
        for header in range(len(lines[0])):
            content = []
            # iterate through each headerline and collect their content in a list
            for column in range(1,len(lines)):
                if lines[column][header].isnumeric(): content.append(int(lines[column][header]))
                else: content.append(lines[column][header])
            # update the dictionary with the header name and a list of values
            self._table.update({lines[0][header]:content})

        # add table number to dictionary
        self._table.update({'tablenumber': tablenumber})


    def rollOn(self, roll:int = 0):
        """!
        This functions rolls on a table and returns the content of the roll result.

        @param a number of a dice roll result. Floating point numbers will be truncated towards zero.
        @return object of the roll result and the content belonging to it.
        """
        # check parameter is a number and receive its int value
        roll = getIntOfNumber(roll)

        # check if table has a roll column
        if self._table.get('roll', False) == False:
            raise ValueError(f"Table number {self._table.get('tablenumber')} does not have a 'roll' column: {self._table.keys()}")

        # initialize variables
        rollResult = {}

        # get list of roll ranges
        rolls = self._table.get('roll')
        # iterate over the list of roll ranges
        for ranges in range(len(rolls)):
            if rolls[ranges] >= roll:
                # putting corresponding 
                for key, value in self._table.items():
                    if 'tablenumber' is key: rollResult.update({key:value})
                    else: rollResult.update({key:value[ranges]})
                break
        
        # replace roll range with true rolled result
        rollResult.update({'roll': roll})
        return TableRollResult(rollResult)