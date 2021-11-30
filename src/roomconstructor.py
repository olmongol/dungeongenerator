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
__updated__ = "30.11.2021"
__author__ = "Marcus Schwamberger"
__me__ = "room prototype constructor"

import json
import os
from tkinter import filedialog
from tkinter.ttk import Combobox
from pprint import pprint
from gui.window import *
from toolbox.confbox import handleConf



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
        @param charlist list of dictionaries holding: player, charname, EPs
        @param datapath path for storing the data into the character files.
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
            self._genericroom = json.load(fp)

        ## @var self.prefix
        # file prefix for type of room:
        # - 'R_': room
        # - 'C_': corridor
        self.prefix = "R_"

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
        savedir = filedialog.asksaveasfilename(defaultextension = ".json",
                                               filetypes = [("Room Files", ".json")],
                                               initialdir = self.roompath)
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


    def __quit(self):
        '''!
        This method closes the window
        '''
        self.window.destroy()


    def __newRoom(self):
        """!
        This resets the frontend to build a new room prototype by the general room prototype

        ----
        @todo this has to be fully implemented.
        """
        self.notdoneyet("__newRoom")


    def __latestID(self, prefix = "R_"):
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



if __name__ == '__main__':
    cfg = handleConf("data/config.ini")
    #-------------- DEBUG
    #pprint(cfg.config.sections())
    #pprint(cfg.config.items("DEFAULT"))
    builder = rgWindow(lang = cfg.config["DEFAULT"]["language"], datapath = cfg.config["DEFAULT"]["datapath"])
