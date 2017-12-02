#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_3.py
# Objective: 
#   Test that a server program can receive a method call using pydbus.
#   The method call receives data from the client.
#   Uses the session bus
#
# Use gdbus to generate the method call
# $ gdbus call --session --dest org.example.demo.test --object-path /org/example/demo/test --method org.example.demo.test.greeting("Bob")
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
import time

# Variables / Constants / Instantiation...
bus = SessionBus()  # SystemBus
BUS = "org.example.demo.test"
loop = GLib.MainLoop()


class DBusService_XML():
    """
    DBus Service XML definition. 
    type="i" for integer, "s" string, "d" double, "as" list of string data.
    """
    dbus = """
    <node>
        <interface name="{}">
            <method name="greeting">
                <arg type="s" name="person" direction="in">
                </arg>
            </method>
        </interface>
    </node>
    """.format(BUS)

    def greeting(self, name):
        "Return Hello and the persons name"
        print("Hello {}".format(name))
        return

if __name__ == "__main__":
    bus.publish(BUS, DBusService_XML())
    loop.run()

