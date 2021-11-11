#!/usr/bin/env python
'''!
\file /home/mongol/git/dungeongenerator/src/toolbox/roombuilder.py
\package toolbox.roombuilder
\brief Tools for building/handling rooms



\date (c) 2021
\copyright GNU V3.0
\author Marcus Schwamberger
\email marcus@lederzeug.de
\version 0.1
'''
import json
import os
from toolbox.logbox import *
from toolbox.confbox import *
__version__ = "0.1"
__updated__ = "11.11.2021"
__author__ = "Marcus Schwamberger"

cfg = handleConf()
logger = createLogger(logger = 'roombuilder', loglvl = 'debug', logsize = '2 MB',
                 count = 5, logpath = cfg.config["DEFAULT"]["logpath"], logfile = 'dungeongenerator.log')



class room():
    """!
    This class will generate a room object with all needed attributes and methods.

    ----
    @todo this has to be fully implemented:
    A room object should have the following attributes:
    - ID
    - room type
    - inhabitants
    - treasures
    - assets/inventory/furniture (with coords)
    - description (multi-language)
    - coordinates of surrounding box
    - absolute coordinates of the bounding box's left upper corner point (starting point)
    - relative coordinates of the room shape (for svg output, maybe even added some
      more SVG options or code snippets)
    - doors/access points with coordinates, orientation and linked rooms/corridors

    and it should have the following methods:
    - method to get all room attributes from saved proto type data files at the
      construction of the room object
    - marking access points/doors on the surrounding box
    - turn the room for given degrees and adapt the surrounding box
    - size the room by a given factor and adapt the surrounding box

    """


    def __init__(self, ID = "R0", roomtype = "204_Guard_Room", coords = [0, 0]):
        """!
        class constructor
        @param ID unique identifier of the room which will be used on the SVG Map
                  and the GM description text/cards later on.
        @param roomtype defines which kind of room it is. This is needed to collect
                        the prototype data from file.
        @param coords the map coordinates of the bounding box's left upper corner
                      point (starting point) which defines the absolute room's
                      position on the final map.
        """
        self.id = ID
        self.type = roomtype
        self.upperleftcorner = coords
        self.inhabitants = None
        self.treasures = None
        self.inventory = None
        self.destcription = f"{ID} {roomtype}\n\n"
        self.shapecoords = None
        self.accesspoints = None
        self.roomfile = cfg.config["DEFAUlT"]["datapath"] + f"/{self.roomtype}.json"

        self.__getRoomData()


    def __getRoomData(self):
        """!
        This method gets the needed room data automatically from the file system
        and sets the room's attributes.

        ----
        @todo copy data from cont into the attributes.
        """
        with open(self.roomfile, "r") as fp:
            cont = json.load(fp)


    def recalcSBox(self):
        """!
        This method will re-calculate the coordinates of the surrounding box
        (rectangle) if the room was turned or sized.

        ----
        @todo check the highest and lowest room shape coordinates for x- and y-axis
        """
        pass
