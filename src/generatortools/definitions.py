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
\version 0.1
'''
__version__ = "0.1"
__updated__ = "28.12.2021"
__author__ = "Marcus Schwamberger"
__me__ = "definitions.py"

## \var dungeoncategory
# this holds the different types of dungeons that may be generated
dungeoncategory = {"en": ["Standard Dungeon", "Fortress Dungeon", "Tomb Dungeon"],
               "de": ["Standarddungeon", "Festungsdungeon", "Grabdungeon"],
               }
## \var roomcategory
# this holds the different types of rooms (by purpose
roomcategory = {"en":["military room", "room for the ruler", "prison room", \
                      "craft room", "living quarter", "room for the dead", \
                      "special room", "storeroom"],
                "de":["militärischer Raum", "Herschaftsraum", "Gefägnisraum", \
                      "Handwerksraum", "Raum d. tägl. Lebens", "Raum der Toten", \
                      "Spezialraum", "Lagerraum"],
                }

