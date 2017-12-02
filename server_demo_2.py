#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_2.py
# Objective: 
#   Test that a server program can receive a method call using pydbus.
#   The method call then sends a time stamp back to the client.
#   Uses the session bus
#
# Use gdbus to generate the method call
# $ gdbus call --session --dest org.example.demo.test --object-path /org/example/demo/test --method org.example.demo.test.get_time_stamp
#
# Ian Stewart
# 2019-11-22
# 
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
            <method name="get_time_stamp">
                <arg type="d" name="response" direction="out">
                </arg>
            </method>
        </interface>
    </node>
    """.format(BUS)

    def get_time_stamp(self):
        "Return a Unix time. Seconds since epoch"
        return time.time() # 1511326564.8677926

if __name__ == "__main__":
    print("Starting Server Demo 2...")
    bus.publish(BUS, DBusService_XML())
    loop.run()

