#!/usr/bin/env python
'''!
\package toolbox.confbox

\brief A toolbox of things to handle config files.


\author Marcus Schwamberger
\date (c) 2021
\version 0.1
\email marcus@lederzeug.de
\license GNU V3.0
'''
import os
import glob
import configparser as cp

from toolbox.logbox import*

__author__ = "Marcus Schwamberger"
__version__ = "0.1"
__updated__ = "12.11.2021"

logger = createLogger(logger = 'confbox',
                      loglvl = 'warning',
                      logsize = '2 MB',
                      count = 2,
                      logpath = glob.glob('../**/log/')[0],
                      logfile = 'confbox.log')



class handleConf():
    """!
    This class handles the usage of config files (INI style)
    """


    def __init__(self):
        """!
        Class constructor: starts search for config file and then implies the
        reading of it.
        """
        self.configfile = self.__getCfile()
        self.readCfg()


    def __getCfile(self):
        """!
        This searches the file system recursively (from a startpoint) for the
        config.ini
        """
        flist = glob.glob("../**/config.ini", recursive = True)

        if len(flist) == 1:
            logger.debug(f"config file at: {flist[0]}")
            return flist[0]

        elif len(flist) > 1:

            for elem in flist:

                if "dungeongenerator" in elem:
                    logger.debug(f"config file at {elem}")
                    return elem

        logger.error(f"no config file found: {flist}")
        raise ValueError("No config file found!")


    def readCfg(self):
        """!
        This method reads the config file and stores it in self.config
        """
        self.config = cp.ConfigParser()
        self.config.read(self.configfile)
        logger.debug(f"{self.configfile} read successfully")
