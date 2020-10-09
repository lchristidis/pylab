#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

user = input("Insert your Username: ")
passcode = getpass("Insert your Password: ")

device1 = { 
    'host' : 'cisco3.lasthop.io',
    'username' : user, 
    'password' : passcode,
    'device_type' : 'cisco_ios',
    'session_log' : 'cisco3_session.txt'
     }

net_connect = ConnectHandler(**device1)

