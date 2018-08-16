#!/usr/bin/python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#import the glade file
builder = Gtk.Builder()
builder.add_from_file("datatransfer.glade")

#class for name entry (both button click and enter)
class Handler:
    def name_enter(self, button):
        print ("Hello world")

builder.connect_signals(Handler())

nameokbutton = builder.get_object("nameokbutton")
window = builder.get_object("window")
namedialog = builder.get_object("namedialog")


"""Old code
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Data Transfer", default-height=300, default-width=500)
#        self.box = Gtk.Box(spacing=0)
#        self.add(self.box)
#        self.orient = Gtk.Orientation(0)
#        self.orient(1)
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)

        self.text = Gtk.Entry()
#        self.add(self.text)
#        self.box.pack_start(self.text, False, False, 5)

        self.button = Gtk.Button(label="Ok")
        self.button.connect("clicked", self.on_button_clicked)
#        self.add(self.button)
#        self.box.pack_start(self.button, False, False, 5)

        self.grid.add(self.text)
        self.grid.add(self.button)
#        self.grid.attach(self.text, 1, 1, 1, 1)
#        self.grid.attach_next_to(self.button, self.text, 3, 1, 1)
        self.add(self.grid)

    def on_button_clicked(self, button):
        print("Hello World")"""

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
