#!/usr/bin/env python
'''!
\file /home/mongol/git/dungeongenerator/src/dungeonmodules/dungeonassets.py
\package dungeonmodules.dungeonassets
\brief Package for dungeon assets like, rooms, doors etc.


\date (c) 2022
\copyright GNU V3.0
\author Marcus Schwamberger
\email marcus@lederzeug.de
\version 0.1
'''
__version__ = "0.1"
__updated__ = "22.05.2022"
__author__ = "Marcus Schwamberger"
__me__ = "dungeonassets.py"

from copy import deepcopy



class accesspoint():
    """! objects of this class are access points to rooms, corridors etc. like
    doorways, gateways etc.
    """


    def __init__(self, **kwargs):
        """!
        Connstructor
        @param kwargs dictionary of key/value pairs:
        - \b id unique object ID
        - \b type of entry:
            - door
            - gate
            - porculli
            - opening
            - secred door
            - dimension portal
        - connects room/corridor id(s) it is connecting
        - description
        - state:
            - closed/open
            - locked
            - broken
            - jammed
        - specials:
            - traps
            - decorations
            - secrets
        - lockstrength (how easy it is to lock pick it)
        - strength (how easy is it to force entry)
        - silence (how quiet it may be opened/closed)
        """
        params = ["id", "type", "connects", "description", "state", "specials", "lockstrength", "strength", "silence"]

        if "id" in kwargs.keys():
            self.id = kwargs["id"]

        else:
            self.id = 0

        if "type" in kwargs.keys():
            self.type = kwargs["type"]
        else:
            self.type = ""

        if "connects" in kwargs.keys():
            self.connects = kwargs["connects"]
        else:
            self.connects = []

        if "description" in kwargs.keys():
            self.description = kwargs["description"]
        else:
            self.description = ""

        if "state" in kwargs.keys():
            self.state = kwargs["state"]
        else:
            self.state = ""

        if "specials" in kwargs.keys():
            self.specials = kwargs["specials"]
        else:
            self.specials = []

        if "lockstrength" in kwargs.keys():
            self.lockstrength = kwargs["lockstrength"]
        else:
            self.lockstrength = 0
        if "strength" in kwargs.keys():
            self.strength = kwargs["strength"]
        else:
            self.strength = 0

        if "silence" in kwargs.keys():
            self.silence = kwargs["silence"]
        else:
            self.silence = 0
