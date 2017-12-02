#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server_demo_7.py
# Objective: 
#   Server program can receive method calls using pydbus.
#   Server program also emits signal with random integer.
#   Uses the system bus.
#
# Requires that /etc/dbus-1/system-local.conf has been added. 
# Contents of system-local.conf at the bottom of this file. 
#
# Warning: Reboot the system for the system-local.conf to take effect.
#
#
# Ian Stewart
# 2019-11-22
# 
# Importing...
import sys
if int(sys.version[0]) < 3: sys.exit("Please use python 3. Exiting...")

# Importing...
from pydbus import SystemBus  # SessionBus
from pydbus.generic import signal
from gi.repository import GLib
import time
import random

# Variables / Constants / Instantiation...
bus = SystemBus()  # SessionBus
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

'''
This is the system-local file after it has had a hole punched in it...

$ cd /etc/dbus-1/
$ ls
session.d  system.d  system-local.conf
$ cat system-local.conf

<!DOCTYPE busconfig PUBLIC "-//freedesktop//DTD D-Bus Bus Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/dbus/1.0/busconfig.dtd">
<busconfig>
  <policy context="default">
    <!-- All users can connect to system bus -->
    <allow user="*"/>

    <!-- Holes must be punched in service configuration files for
         name ownership and sending method calls -->
    <!-- Disable the deny. Ian - Nov 2017...
    <deny own="*"/>
    <deny send_type="method_call"/> -->

    <!-- Change to allow. Ian - Nov 2017 -->
    <allow own="*"/>
    <allow send_type="method_call"/>

    <!-- Signals and reply messages (method returns, errors) are allowed
         by default -->
    <allow send_type="signal"/>
    <allow send_requested_reply="true" send_type="method_return"/>
    <allow send_requested_reply="true" send_type="error"/>

    <!-- All messages may be received by default -->
    <allow receive_type="method_call"/>
    <allow receive_type="method_return"/>
    <allow receive_type="error"/>
    <allow receive_type="signal"/>

    <!-- Allow anyone to talk to the message bus -->
    <allow send_destination="org.freedesktop.DBus"
           send_interface="org.freedesktop.DBus" />
    <allow send_destination="org.freedesktop.DBus"
           send_interface="org.freedesktop.DBus.Introspectable"/>
    <!-- But disallow some specific bus services -->
    <deny send_destination="org.freedesktop.DBus"
          send_interface="org.freedesktop.DBus"
          send_member="UpdateActivationEnvironment"/>
    <deny send_destination="org.freedesktop.DBus"
          send_interface="org.freedesktop.DBus.Debug.Stats"/>
    <deny send_destination="org.freedesktop.DBus"
          send_interface="org.freedesktop.systemd1.Activator"/>
  </policy>
</busconfig>

'''
