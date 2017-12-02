#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_4.py
# Objective: 
#   Test that a server program can receive a method call using pydbus.
#   The method call received string data and then sends the string back.
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
            <method name="echo_string">
                <arg type="s" name="input" direction="in">
                </arg>
                <arg type="s" name="output" direction="out">
                </arg>
            </method>
        </interface>
    </node>
    """.format(BUS)

    def echo_string(self, input_string):
        "Echo the string"
        return input_string


if __name__ == "__main__":
    bus.publish(BUS, DBusService_XML())
    loop.run()

