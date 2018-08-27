#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import call
import subprocess
import sys
import os

#open glade file
builder = Gtk.Builder()
builder.add_from_file("datatransfer.glade")
"""
if len(sys.argv) == 2:
    devname = sys.argv[1]
    print("devname (python) = "+ devname)
else:
    print("Error: no device specified")
    sys.exit()
"""
#get widgets from the builder
okbutton = builder.get_object("okbutton")
nameentry = builder.get_object("nameentry")
window = builder.get_object("main")
filechooser = builder.get_object("filechooser")
spinner = builder.get_object("spinner")
dirsizelabel = builder.get_object("dirsizelabel")

class Handler: #handles events from the builder
    def ok_button(self, data):
        name = nameentry.get_text()
        path = str(filechooser.get_filename())
        is_path(path)
    
    def dir_change(self, data):
#        spinner.show()
        spinner.start()
        path = str(filechooser.get_filename())
        get_size(path)
#        message(window, "Path changed to: " + path)
       
#functions
def message(parent, message): #message dialog box
    dialog = Gtk.MessageDialog(parent, 0, Gtk.MessageType.INFO,
        Gtk.ButtonsType.OK, message)
    dialog.run()
    dialog.destroy()

def is_path(path): #checks if a string is a valid path and if that path is a directory or not
    if os.path.exists(path) == True:
        if os.path.isdir(path) == True:
#            print("path is " + path)
            get_size(path)
        else:
            message(window, "Error: path is not a directory")
    else:
        message(window, "Error: invalid path")

def get_size(path): #call shell script to get the size of the directory
#    call(["./disk.sh", "--get-size", path])    #deprecated
    cmd1 = subprocess.Popen(["du", "-sh", path], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    message(window, cmd1.communicate()[0])
#   print(cmd1.stdout)

#filechooser.set_current_folder("/home")
builder.connect_signals(Handler())

window.connect("destroy", Gtk.main_quit)
window.show()
Gtk.main()
