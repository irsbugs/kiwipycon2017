#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_1.py
# Objective: 
#   Test that a server program can receive a method call using pydbus.
#   The method call passes no arguments.
#   Uses the session bus
#
# Use gdbus to generate the method call
# $ gdbus call --session --dest org.example.demo.test --object-path /org/example/demo/test --method org.example.demo.test.server_no_args
#
# Ian Stewart
# 2019-11-22
# 
# Importing...
import sys
if int(sys.version[0]) < 3: sys.exit("Please use python 3. Exiting...")

# Importing...
from pydbus import SessionBus  # SystemBus
from gi.repository import GLib

# Variables / Constants / Instantiation...
bus = SessionBus()  # SystemBus
BUS = "org.example.demo.test"
loop = GLib.MainLoop()
message_count = 0


class DBusService_XML():
    """
    DBus Service XML definition. 
    type="i" for integer, "s" string, "d" double, "as" list of string data.
    """
    dbus = """
    <node>
        <interface name="{}">
            <method name="server_no_args">
            </method>
        </interface>
    </node>
    """.format(BUS)

    def server_no_args(self):
        "No arguments over the dbus. Server produces a message on the console."
        global message_count
        print("This is message {}".format(message_count))
        message_count +=1
        return

if __name__ == "__main__":
    print("Starting Server Demo 1...")
    bus.publish(BUS, DBusService_XML())
    loop.run()
