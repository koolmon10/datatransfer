#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import call
import sys

builder = Gtk.Builder()
builder.add_from_file("datatransfer.glade")

if len(sys.argv) == 2:
    devname = sys.argv[1]
    print ("devname (python) = "+ devname)
else:
    print("Error: no device specified")
    sys.exit()

#get widgets from the builder
nameokbutton = builder.get_object("nameokbutton")
nameentry = builder.get_object("nameentry")
window = builder.get_object("window")
namedialog = builder.get_object("namedialog")

#class to interact with the data
def get_size():
    call(["./disk.sh", devname])

#class for name entry (both button click and enter)
class Handler:
    def name_enter(self, button):
        name = nameentry.get_text()
        print (name)
#testing code         call(["touch", name])

get_size()
builder.connect_signals(Handler())

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
