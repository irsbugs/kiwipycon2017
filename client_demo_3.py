#!/usr/bin/env python3
#!
# client_demo_3.py
# Client sends data to the server. Server prints the data. 
#
# Ian Stewart
# 2019-11-22
#
# Importing...
from pydbus import SessionBus  # from pydbus import SystemBus
from gi.repository import GLib
import random

# Instantiation, Constants, Variables...
bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call_client_3():
    "Client sends a random name to the server."
    name_list = ["Bob", "Pete", "Fred", "Sue", "Wendy"]
    name = name_list[random.randint(0, len(name_list)-1)]
    reply = server_object.greeting(name)
    return True

if __name__=="__main__":
    print("Starting Client Demo 3...")
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_3)
    loop.run()

"""
Notes:
1. Launch server_demo_3.py in one console
2. Then launch client_demo_3.py in another console
"""
