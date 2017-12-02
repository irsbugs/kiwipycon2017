#!/usr/bin/env python3
#!
# client_demo_5.py
# Objective: Receive random numbers emitted by server.
#
# Ian Stewart
# 2019-11-22
#
# Importing...
from pydbus import SessionBus  # from pydbus import SystemBus
from gi.repository import GLib
# Instantiation, Constants, Variables...
bus = SessionBus()
BUS = "org.example.demo.test"
loop = GLib.MainLoop()

def cb_signal_emission(*args):
    "Callback on emitting signal, a random integer, from server. "
    # Data is in args[4]. The first item in a tuple. i.e. args[4][0]
    # print(args)
    random_number = args[4][0]
    print("Client received random number: {}".format(random_number))

if __name__=="__main__":
    print("Starting. Client Demo 5..")
    # Create the dbus filter based on: org.example.demo.test
    dbus_filter = "/" + "/".join(BUS.split("."))
    print(dbus_filter)
    # Subscribe to dbus to monitor for server signal emissions
    # dbus_filter. E.g. /org/example/demo/test
    bus.subscribe(object = dbus_filter, signal_fired = cb_signal_emission)
    loop.run()

"""
Notes:
1. Launch server_demo_5.py in one console
2. Then launch client_demo_5.py in another console
"""
