#!/usr/bin/env python
'''!
\package generatortools.definitions
\brief Dungeon, room, door and other definitions.

 This package holds al type of definitons needed for the dungeon generator such
 as room category etc.
\date (c) 2021
\copyright GNU V3.0
\author Marcus Schwamberger
\email marcus@lederzeug.de
\version 0.2
'''
__version__ = "0.2"
__updated__ = "14.05.2022"
__author__ = "Marcus Schwamberger"
__me__ = "definitions.py"

## \var dungeoncategory
# this holds the different types of dungeons that may be generated
dungeoncategory = {"en": ["Standard Dungeon", "Fortress Dungeon", "Tomb Dungeon"],
               "de": ["Standarddungeon", "Festungsdungeon", "Grabdungeon"],
               }
## \var roomcategory
# this holds the different types of rooms (by purpose
roomcategory = {"en":["military rooms", "rooms for the ruler", "prison rooms", \
                      "craft rooms", "living quarters", "rooms for the dead", \
                      "special rooms", "storerooms", "own defined rooms"],
                "de":[r"militärische Räume", r"Herschaftsräume", "Gefägnisräume", \
                      "Handwerksräume", "Räume d. tägl. Lebens", "Räume der Toten", \
                      "Spezialräume", "Lagerräume", "selbst definierte Räume"],
                }
## \var tableidranges
# this dictionary defines the ID range of tables to a specific category.
tableidranges = {"doors and corridors":(150, 199),
                 "military room": (200, 250),
                 "prison rooms": (251, 300),
                 "craft rooms": (301, 350),
                 "living quarters": (351, 400),
                 "rooms for the ruler": (401, 450),
                 "rooms for the dead": (451, 500),
                 "special rooms":(501, 550),
                 "storerooms": (551, 600),
                 "own defined rooms":(601, 700),
                 "dungeon history":(701, 800),
                 "dungeon abandonment":(801, 900)
                 }
