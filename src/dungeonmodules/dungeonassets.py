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
__updated__ = "20.05.2022"
__author__ = "Marcus Schwamberger"
__me__ = "dungeonassets.py"



class access ():
    """! objects of this class are access points to rooms, corridors etc. like
    doorways, gateways etc.
    """


    def __init__(self, **kargs):
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
        pass
