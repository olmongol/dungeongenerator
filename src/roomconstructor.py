#!/usr/bin/env python
'''!
\file roomconstructor.py

\brief Helper tool to construct room prototypes

This is a tool to build room prototype files by GUI.

\date (c) 2021
\copyright GNU V3.0
\author Marcus Schwamberger
\email marcus@lederzeug.de
\version 0.1
'''
__version__ = "0.1"
__updated__ = "28.12.2021"
__author__ = "Marcus Schwamberger"
__me__ = "room prototype constructor"

import json
import os
import tkinter as tk
from tkinter import filedialog, Text
from tkinter.ttk import Combobox
from pprint import pprint
import copy as cp
from random import randint

from gui.window import *
from toolbox.confbox import handleConf
from toolbox.generaltools import filesInDir
from generatortools.definitions import roomcategory



class rgWindow(blankWindow):
    """!
    This is a GUI for the construction of room prototype data files.
    """


    def __init__(self, lang = "en", datapath = "./data", roompath = ""):
        """!
        Class constructor
        @param lang The chosen language for window's and button's
                    texts. At the moment, only English (en, default
                    value) and German (de) are supported.
        @param roompath path for storing the room's data (templates) into
        @param datapath path for storing the general data into.
        """

        ## @var self.lang
        # this attribute holds the language code for the multi-language support
        self.lang = lang
        ## @var self.datapath
        # this attribute holds the path to the 'root' data dir.
        self.datapath = datapath

        if roompath:
            ## @var self.roompath
            # the data path where the rooms where stored (if not in default)
            self.roompath = roompath

        else:
            self.roompath = f"{self.datapath}/rooms"

        with open(f"{self.roompath}/R-0_generic_room.json") as fp:
            ##\var self._genericroom
            # this holds a prototype/generic room (loaded from file)
            self._genericroom = json.load(fp)

        ##\var self.room
        # this attribute holds the current room data (dict/JSON)
        self.room = cp.deepcopy(self._genericroom)

        ## @var self.prefix
        # file prefix for type of room:
        # - 'R-': room
        # - 'C-': corridor
        # - 'T-': Trap
        # - 'S-' : Special
        # - 'D-' : Door
        self.prefix = "R-"

        self.initialfilename = "dummy.json"
        #
        blankWindow.__init__(self, self.lang)
        self.window.title(wintitle["room builder"][self.lang])
        self.__addFileMenu()
        self.__addEditMenu()
        self.__addHelpMenu()
        self.__buildWin()
        self.window.mainloop()


    def __addFileMenu(self):
        '''!
        This methods adds the file menu bar to the window
        '''
        self.filemenu = Menu(master = self.menu)
        self.menu.add_cascade(label = txtmenu['menu_file'][self.lang],
                              menu = self.filemenu)
        self.filemenu.add_command(label = submenu['file'][self.lang]["new"],
                                  command = self.__newRoom)
        self.filemenu.add_command(label = submenu['file'][self.lang]['open'],
                                  command = self.__open)
        self.filemenu.add_command(label = submenu['file'][self.lang]['save'],
                                  command = self.__save)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = submenu['file'][self.lang]['quit'],
                                  command = self.__quit)


    def __addEditMenu(self):
        '''!
        This method asds the edit menu to the window's menu bar
        '''
        self.editmenu = Menu(master = self.menu)
        self.menu.add_cascade(label = txtmenu["menu_edit"][self.lang],
                              menu = self.editmenu)
        self.editmenu.add_command(label = submenu['edit'][self.lang]['draw room'],
                                  command = self.__drawroom)
        self.editmenu.add_command(label = submenu['edit'][self.lang]['add param'],
                                  command = self.__addparam)
        self.editmenu.add_command(label = submenu['edit'][self.lang]['add spec'],
                                  command = self.__addspec)


    def __drawroom(self):
        '''!
        This method opens another window to draw the room shape

        ----
        @todo has to be implemented fully
        '''
        self.notdoneyet("__drawroom")


    def __addparam(self):
        '''!
        This adds a parameter to the defaults of a room/corridor.

        ----
        @todo this has to be implemented fully
        '''
        self.notdoneyet("__addparam")


    def __addspec(self):
        '''!
        This adds a special option/item to  a room/corridor.

        ----
        @todo this has to be implemented fully
        '''
        self.notdoneyet("__addspec")


    def __addHelpMenu(self):
        """!
        This methods defines a help menu.
        """
        self.helpmenu = Menu(master = self.menu)
        self.menu.add_cascade(label = txtmenu['help'][self.lang],
                              menu = self.helpmenu)

        self.helpmenu.add_separator()
        self.helpmenu.add_command(label = submenu['help'][self.lang]['about_rc'],
                                  command = self._helpAbout)


    def __save(self):
        '''!
        This opens a file dialog window for saving
        '''
        self.updateRoomdata()
        savedir = filedialog.asksaveasfilename(defaultextension = ".json",
                                               filetypes = [("Room Files", ".json")],
                                               initialdir = self.roompath,
                                               initialfile = self.initialfilename)
        with open(savedir, "w") as fp:
            json.dump(self.room, fp, indent = 4)


    def __open(self):
        '''!
        This opens a file dialog window for opening a group file.
        '''
        opendir = filedialog.askopenfilename(defaultextension = ".json",
                                             filetypes = [("Room Files", ".json")],
                                             initialdir = self.roompath)
        with open(opendir, "r") as fp:
            self.room = json.load(fp)

        self.updateDisplay()


    def __quit(self):
        '''!
        This method closes the window
        '''
        self.window.destroy()


    def __getRoomList(self):
        """!
        This method gets all defined rooms in the default room data directory by name:
         - R_<id & name>.json (Room)
         - C_<id & name>.json (corridor)
         - S_<id & name>.json (speciality)
         - T_<id & name>.json <trap>


         ----
         @todo this has to be fully implemented
         - finding all files by regex
         - build a list of rooms
        """

        ## \var self roomdefs
        # this contains a list of predefined room names
        self.roomdefs = filesInDir(folder = self.roompath, filenames = "R_*.json") + \
                        filesInDir(folder = self.roompath, filenames = "C_*.json")


    def _getRandom(self):
        """!
        This evaluates random numbers for width & length of a room if there are ranges
        given.
        """
        coords = {}
        max = [0, 0]

        for c in range(0, len(self.room["corners"])):

            for i in range(0, 2):

                if type(self.room["corners"][c][i]) != int:

                    if type(self.room["corners"][c][i]) == str:

                        if "=" in self.room["corners"][c][i]:
                            key, value = self.room["corners"][c][i].split("=")

                            if "-" in value:
                                lower, upper = value.split("-")
                                value = randint(int(lower), int(upper))

                            else:
                                value = int(value)

                            coords[key] = value
                            self.room["corners"][c][i] = value
                            if max[i] < value:
                                max[i] = value

                        if self.room["corners"][c][i] in coords.keys():
                            self.room["corners"][c][i] = coords[self.room["corners"][c][i]]
                else:
                    if max[i] < self.room["corners"][c][i]:
                        max[i] = self.room["corners"][c][i]

        if max != [0, 0]:
            self.room["box coords"][1][1] = max[1]
            self.room["box coords"][2][0] = max[0]
            self.room["box coords"][3] = max
        self.updateDisplay()


    def __determineBox(self):
        """!
        This calculates the corners of the surrounding box
        """
        max = [0, 0]
        origin = self.room["corners"][0]
        for c in range(0, len(self.room["corners"])):

            if origin[0] >= self.room["corners"][c][0] and origin[1] >= self.room["corners"][c][1]:
                origin = self.room["corners"][c]

            for i in range(0, 2):

                if max[i] <= self.room["corners"][c][i]:
                    max[i] = self.room["corners"][c][i]

        self.room["origin"] = cp.deepcopy(origin)

        if max != [0, 0]:
            self.room["box coords"][1][1] = max[1]
            self.room["box coords"][2][0] = max[0]
            self.room["box coords"][3] = max

        self.updateDisplay()


    def updateRoomdata(self):
        """!
        This updates all room data in self.room and the self.initialfilename.

        ----
        @todo this has to be implemented fully
         - <strike>set self.initialfilename</strike>
         - get all Entry field changes
        """
        #self._getRandom()

        self.room["id"] = self.id.get()
        self.room["name"] = self.name.get()
        self.room["room type"] = self.selectType.get()
        self.room["shape"] = self.selectShape.get()
        name = self.room["name"].replace(" ", "_")
        self.initialfilename = f'{self.room["id"]}_{name}.json'
        self.__determineBox()


    def updateDisplay(self):
        """!
        This updates all displayed data

        ----
        @todo this has to be fully implemented:
        # <strike>update corners</strike>
        # <strike>update id</strike>
        # <strike>update name</strike>
        # <strike>update surrounding box</strike>
        # update description
        # <strike>update room type</strike>
        # <strike>update shape</strike>
        # update number of doors
        # update doors
        # update openings
        # update assets
        # update inhabitants
        # update treasures
        """
        self.id.set(str(self.room["id"]))
        self.rwidth.set(str(self.room["box coords"][3][0]))
        self.rlength.set(str(self.room["box coords"][3][1]))
        self.rcorners.set(str(self.room["corners"]))
        self.selectShape.set(self.room["shape"])
        self.selectType.set(self.room["room type"])


    def _updateCorners(self):
        """!
        This method parses a list from the corners' Entry field.
        """
        stringlist = self.rcorners.get()

        stringlist = stringlist[1:-1].split("],")

        for i in range(0, len(stringlist)):
            stringlist[i] = stringlist[i].strip("[]' ")
            stringlist[i] = stringlist[i].split(",")

            for j in range(0, len(stringlist[i])):
                stringlist[i][j] = stringlist[i][j].strip("[]' ")

                try:
                    stringlist[i][j] = int(stringlist[i][j])
                except:
                    pass
        self.room["corners"] = cp.deepcopy(stringlist)
        self.updateRoomdata()
        self.updateDisplay()


    def __newRoom(self):
        """!
        This resets the frontend to build a new room prototype by the general room prototype

        ----
        @todo this has to be fully implemented.
        """
        self.notdoneyet("__newRoom")


    def __latestID(self, prefix = "R-"):
        """!
        This gets the highest prototype file ID from self.roompath

        @param prefix of roomtype to search for.

        ----
        @todo the check intelligence has to be implementet.
        """
        result = 0
        return result


    def __buildWin(self):
        """!
        This method builds the all the elements of the GUI frontend

        ----
        @todo this has to be planed an implemented fully:
        """
        #-------- row 0

        Label(self.window,
              text = "ID: "
              ).grid(column = 0, row = 0, sticky = W)

        self.id = StringVar()
        self.id.set(f"{self.prefix}{self.__latestID(prefix = self.prefix)}")
        Entry(self.window,
              textvariable = self.id,
              width = 8
              ).grid(row = 0, column = 1, sticky = "EW")

        Label(self.window,
              text = f" {labels['name'][self.lang]}:",
              ).grid(row = 0, column = 2, sticky = "EW")

        self.name = StringVar()
        self.name.set(self._genericroom['name'])
        Entry(self.window,
              textvariable = self.name,
              width = 20
              ).grid(row = 0, column = 3, sticky = "EW")

        Label(self.window,
              text = f" {labels['type'][self.lang]}:"
              ).grid(row = 0, column = 4, sticky = "EW")
        self.selectType = StringVar()
        self.selectType.set(self._genericroom["room type"])
        self.__typeCombo = Combobox(self.window,
                                   textvariable = self.selectType,
                                   values = labels["room types"][self.lang])
        self.__typeCombo.grid(row = 0, column = 5, sticky = W)

        Label(self.window,
              text = f" {labels['shape'][self.lang]}:"
              ).grid(row = 0, column = 6, sticky = W)
        self.selectShape = StringVar()
        self.selectShape.set(self._genericroom["shape"])
        self.__shapeCombo = Combobox(self.window,
                                   textvariable = self.selectShape,
                                   values = labels["room shape"][self.lang]
                                   )
        self.__shapeCombo.grid(row = 0, column = 7, sticky = "EW")

        #---------- row 1
        Label(self.window,
              text = f" {labels['size'][self.lang]} ({labels['sbox'][self.lang]}):"
              ).grid(row = 1, column = 0, columnspan = 2, sticky = W)
        self

        Label(self.window,
              text = f"{labels['width'][self.lang]}: "
              ).grid(row = 1, column = 2, sticky = W)

        self.rwidth = StringVar()
        self.rwidth.set(self._genericroom["corners"][1][0])
        Entry(self.window,
              textvariable = self.rwidth,
              width = 10
              ).grid(row = 1, column = 3, sticky = "WE")

        Label(self.window,
              text = f"{labels['length'][self.lang]}: "
              ).grid(row = 1, column = 4, sticky = W)

        self.rlength = StringVar()
        self.rlength.set(self._genericroom["corners"][0][1])
        Entry(self.window,
              textvariable = self.rlength,
              width = 10
              ).grid(row = 1, column = 5, sticky = "WE")

        Button(self.window,
               text = txtbutton["but_roll"][self.lang],
               command = self._getRandom
               ).grid(row = 1, column = 6, sticky = "EW")

        #---------- row 2
        Label(self.window,
              text = labels["corners"][self.lang] + ": "
              ).grid(row = 2, column = 0, sticky = W)

        self.rcorners = StringVar()
        self.rcorners.set(str(self.room["corners"]))
        Entry(self.window,
               textvariable = self.rcorners,
               width = 50
               ).grid(row = 2, column = 1, columnspan = 5, sticky = "EW")

        Button(self.window,
               text = txtbutton["but_take"][self.lang],
               command = self._updateCorners
               ).grid(row = 2, column = 6, sticky = "EW")

        #---------- row 3

        #---------- row 5
        Label(self.window,
              text = f"{labels['description'][self.lang]}:"
              ).grid(row = 5, column = 0, sticky = "WS")
        #self.description = StringVar()
        #self.description.set(self._genericroom["description"])
        self.__descrText = Text(self.window,
                                height = 20,
                                width = 90
                                )
        self.__descrText.grid(row = 5, column = 0,
                                       columnspan = 8,
                                       sticky = "NEWS")
        #self.__descrText.insert(tk.END, self._genericroom["description"])
        self.__descrText.insert(END, self._genericroom["description"])



if __name__ == '__main__':
    cfg = handleConf("data/config.ini")
    #-------------- DEBUG
    #pprint(cfg.config.sections())
    #pprint(cfg.config.items("DEFAULT"))
    builder = rgWindow(lang = cfg.config["DEFAULT"]["language"], datapath = cfg.config["DEFAULT"]["datapath"])
