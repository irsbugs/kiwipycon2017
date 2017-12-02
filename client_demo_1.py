#!/usr/bin/env python3
#!
# client_demo_1.py
# Client sends a method call to the Server, but no arguments are passed.
# Server prints a message.
#
# Ian Stewart
# 2019-11-22
#
# Importing...
from pydbus import SessionBus  # from pydbus import SystemBus
from gi.repository import GLib

# Instantiation, Constants , Variables...
bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call_client_1():
    print("Sending Method Call: server_no_args")
    reply = server_object.server_no_args()
    return True

if __name__=="__main__":
    print("Starting Client Demo 1...")
    # Call function to make a method call.
    GLib.timeout_add_seconds(interval=INTERVAL, 
                             function=make_method_call_client_1)
    loop.run()

'''
Notes:
1. Launch server_demo_1.py in one console
2. Then launch client_demo_1.py in another console.
'''
