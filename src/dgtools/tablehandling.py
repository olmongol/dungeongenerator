'''!
\package dgtools.tablehandling

\brief Tool to handle tables and table roll results.

\date (c) 2021
\copyright GNU V3.0
\author mambano
\version 0.1

@todo the following has to be fully implemented
- add logging
- optimise file reading by avoiding a list as temporary structure
- tuples of additional properties like 'tablenumber' for an easy handling
- dot description of csv file reading
'''

from toolbox.generaltools import textFileReader, getIntOfNumber
import csv

class Table(): 
    """!
    This Class handles reading a table from file and provides several operations for it.
    """
    def __init__(self, tablenumber = 100):
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
                # add content by header from column as integer if it is numeric
                if lines[column][header].isnumeric(): content.append(int(lines[column][header]))
                # add content by header from column as string with trailing whitespace removed 
                else: content.append(str(lines[column][header]).rstrip())
            # update the dictionary with the header name, where trailing whitespace are removed, and a list of values
            self._table.update({str(lines[0][header]).rstrip():content})

        # add table number to dictionary
        self._table.update({'tablenumber': tablenumber})


    def rollOn(self, roll = 0):
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
                    if 'tablenumber' == key: rollResult.update({key:value})
                    else: rollResult.update({key:value[ranges]})
                break
        
        # replace roll range with true rolled result
        rollResult.update({'roll': roll})
        return TableRollResult(rollResult)


class TableRollResult():
    """!
    This Class represent the content of a roll result on a table.
    """
    def __init__(self, rollresult = {}):
        if type(rollresult) == None: raise TypeError(f"Parameter 'rollresult' is of type 'None', no processing possible!")
        else: self._rollresult = rollresult

    @property
    def rollresult(self):
        """!
        Returns the object representation of the 'TabelRollResult'.
        """
        return self._rollresult

    def __str__(self) -> str:
        """!
        Returns a readable string representation of the 'TabelRollResult'.
        """
        return str(self._rollresult)