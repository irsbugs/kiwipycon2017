#!/usr/bin/env python3
#!
# client_demo_2.py
# Client performs method call and receives time stamp from the server.
#
# Ian Stewart
# 2019-11-22
#
# Importing.
from pydbus import SessionBus  # from pydbus import SystemBus
from gi.repository import GLib

# Instantiation, Constants, Variables... 
bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2

def make_method_call_client_2():
    "Server returns a time stamp."
    reply = server_object.get_time_stamp()
    print("Returned data is of type: {}".format(type(reply)))
    print("Time stamp received from server: {}".format(reply))
    return True

if __name__=="__main__":
    print("Starting Client Demo 2...")
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_2)
    loop.run()

"""
Notes:
1. Launch server_demo_2.py in one console
2. Then launch client_demo_2.py in another console.
"""
