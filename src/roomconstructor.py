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
__updated__ = "28.11.2021"
__author__ = "Marcus Schwamberger"
__me__ = "room prototype constructor"

import json
import os
from tkinter import filedialog
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

        blankWindow.__init__(self, self.lang)
        self.window.title("Room Prototype Constructor")
        self.__addMenu()
        self.__addHelpMenu()
        self.__buildWin()
        self.window.mainloop()


    def __addMenu(self):
        '''!
        This methods adds the menu bar to the window
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


    def __buildWin(self):
        """!
        This method builds the all the elements of the GUI frontend

        ----
        @todo this has to be planed an implemented fully.
        """
        self.notdoneyet("__buildwin")



if __name__ == '__main__':
    cfg = handleConf("data/config.ini")
    pprint(cfg.config.sections())
    pprint(cfg.config.items("DEFAULT"))
    builder = rgWindow(lang = cfg.config["DEFAULT"]["language"], datapath = cfg.config["DEFAULT"]["datapath"])
