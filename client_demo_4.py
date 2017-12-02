#!/usr/bin/env python3
#!
# client_demo_4.py
# Objective: Echo a string
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

def make_method_call_client_4():
    name_list = ["Bob", "Pete", "Fred", "Sue", "Wendy"]
    name = name_list[random.randint(0, len(name_list)-1)]
    print("Name to be sent to server: {}".format(name))
    reply = server_object.echo_string(name)
    print("Message echoed from server: {}".format(reply))
    return True

if __name__=="__main__":
    print("Starting Client Demo 4...")
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_4)
    loop.run()

"""
Notes:
1. Launch server_demo_4.py in one console
2. Then launch client_demo_4.py in another console
"""
