#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_5.py
# Objective: 
#   Test that a server program can emit an integer using pydbus.
#   Uses the session bus
#
# Use gdbus to monitor the signals being emitted.
# $ gdbus monitor --session --dest org.example.demo.test
#
# Ian Stewart
# 2019-11-22
# 
# Importing...
import sys
if int(sys.version[0]) < 3: sys.exit("Please use python 3. Exiting...")

# Importing...
from pydbus import SessionBus  # SystemBus
from pydbus.generic import signal
from gi.repository import GLib
import time
import random

# Variables / Constants / Instantiation...
bus = SessionBus()  # SystemBus
BUS = "org.example.demo.test"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0


class DBusService_XML():
    """
    DBus Service XML definition. 
    type="i" for integer, "s" string, "d" double, "as" list of string data.
    """
    dbus = """
    <node>
        <interface name="{}">
            <signal name="integer_signal">
                <arg type="i"/>
            </signal>
        </interface>
    </node>
    """.format(BUS)
    integer_signal = signal()

def timer():
    "Emit a random integer each call."
    random_integer = random.randint(0, 100)
    print("Random integer emitted: {}".format(random_integer))
    emit.integer_signal(random_integer)
    return True       

if __name__ == "__main__":
    print("Starting Server Demo 5...")
    emit = DBusService_XML()
    bus.publish(BUS, emit)

    GLib.timeout_add_seconds(interval=INTERVAL, function=timer)
    loop.run()

