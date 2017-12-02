#!/usr/bin/env python3
#!
# client_demo_7.py
# Objective: Perform 4 x Call Method, 1 x Subcribe to emission. 
#           Uses the System D-Bus
#
# Ian Stewart
# 2019-11-22
#
# Importing...
from pydbus import SystemBus  # from pydbus import SessionBus
from gi.repository import GLib 
import random

# Instantiation, Constants, Variables... 
bus = SystemBus()
BUS = "org.example.demo.test"
# Provide for method calls.
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 4

def cb_signal_emission(*args):
    """
    Callback on emitting signal from server
    Emitted signal a random integer
    Data is in args[4]. The first item in a tuple.args[4][0]
    """
    #print(args)
    random_number = args[4][0]
    print("Emitted: Client received random number: {}".format(random_number))

def make_method_call_client_4():
    #    string = input("Enter a string for the server to echo: ")
    string = chr(random.randint(65, 90))
    reply = server_object.echo_string(string)
    #print("Returned data is of type: {}".format(type(reply)))
    print("Client_4: Data Sent: {} Echoed data: {}".format(string, reply))
    return True

def make_method_call_client_3():
    "Send a text string to the server"
    name_list = ["Bob", "Pete", "Fred", "Sue", "Wendy"]
    name = name_list[random.randint(0, len(name_list)-1)]
    reply = server_object.greeting(name)
    return True

def make_method_call_client_2():
    "Server returns a time stamp."
    reply = server_object.get_time_stamp()
    #print("Returned data is of type: {}".format(type(reply)))
    print("Client 2: Time stamp received from server: {}".format(reply))
    return True

def make_method_call_client_1():
    "No args passed. Server outputs."
    print("Sending Method Call: server_no_args")
    reply = server_object.server_no_args()
    #print(reply)  # reply = None
    return True

def main_method():
    # Call the 4 x method calls
    make_method_call_client_1()    
    make_method_call_client_2()
    make_method_call_client_3()
    make_method_call_client_4()
    return True

if __name__=="__main__":
    print("Starting...")

    # Create the dbus filter based on: org.example.demo.test
    dbus_filter = "/" + "/".join(BUS.split("."))
    #print(dbus_filter)

    # Subscribe to dbus to monitor for server signal emissions
    # dbus_filter. E.g. /org/example/demo/test
    bus.subscribe(object = dbus_filter, signal_fired = cb_signal_emission)

    # Call function to make a method call
    GLib.timeout_add_seconds(interval=INTERVAL, function=main_method)

    loop.run()

"""
Notes:
1. Launch server_demo_7.py in one console
2. Then launch client_demo_7.py in another console.
"""
