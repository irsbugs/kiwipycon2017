#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_6.py
# Objective: 
#   Server program can receive 4 x method calls using pydbus.
#   Server program also emits signal with random integer.
#   Uses the session bus
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
            <method name="echo_string">
                <arg type="s" name="input" direction="in">
                </arg>
                <arg type="s" name="output" direction="out">
                </arg>
            </method>
            <method name="greeting">
                <arg type="s" name="person" direction="in">
                </arg>
            </method>
            <method name="get_time_stamp">
                <arg type="d" name="response" direction="out">
                </arg>
            </method>
            <method name="server_no_args">
            </method>
        </interface>
    </node>
    """.format(BUS)
    integer_signal = signal()

    def echo_string(self, input_string):
        "From Client 4. Echo the string"
        return input_string

    def greeting(self, name):
        "From Cleint 3. Return Hello and the persons name"
        print("From Client 3: Hello {}".format(name))
        return

    def get_time_stamp(self):
        "From Client 2. Return a Unix time. Seconds since epoch"
        return time.time() # 1511326564.8677926

    def server_no_args(self):
        "From Client 1. No arguments, Server has a message on the console."
        global message_count
        print("From Client 1: This is message {}".format(message_count))
        message_count +=1
        return

def timer():
    "Emit a random integer each call."
    random_integer = random.randint(0, 100)
    print("Random integer emitted: {}".format(random_integer))
    emit.integer_signal(random_integer)
    return True
        

if __name__ == "__main__":
    emit = DBusService_XML()
    bus.publish(BUS, emit)

    GLib.timeout_add_seconds(interval=INTERVAL, function=timer)
    loop.run()

