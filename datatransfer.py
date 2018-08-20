#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import call
import sys
import os

builder = Gtk.Builder()
builder.add_from_file("datatransfer.glade")
"""
if len(sys.argv) == 2:
    devname = sys.argv[1]
    print ("devname (python) = "+ devname)
else:
    print("Error: no device specified")
    sys.exit()
"""
#get widgets from the builder
nameokbutton = builder.get_object("nameokbutton")
nameentry = builder.get_object("nameentry")
window = builder.get_object("window")

#functions
def message(parent, message): #message dialog box
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.INFO,
        Gtk.ButtonsType.OK, message)
    dialog.run()
    dialog.destroy()
        
def is_path(path): #checks if a string is a valid path and if that path is a directory or not
    if os.path.exists(path) == True:
        if os.path.isdir(path) == True:
            message(window, "A winner is you!")
        else:
            message(window, "Error: path is not a directory")
    else:
        message(window, "Error: path does not exist")

def get_size(dirname):
    call(["./disk.sh", "--get-size", dirname])

#class for name entry (both button click and enter)
class Handler:
    def name_enter(self, button):
        name = nameentry.get_text()
        is_path(name)

builder.connect_signals(Handler())

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
