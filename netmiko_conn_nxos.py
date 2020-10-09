#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass

user = input("Insert your Python class Username: ")
passcode = getpass("Insert your Password: ")

device1 = { 
    'host' : 'nxos1.lasthop.io',
    'username' : user, 
    'password' : passcode,
    'device_type' : 'cisco_nxos',
    'session_log' : 'nxos1_session.txt'
    }
     
device2 = {
      'host' : 'nxos2.lasthop.io',
      'username' : user,
      'password' : passcode,
      'device_type' : 'cisco_nxos',
      'session_log' : 'nxos2_session.txt'
      }



net_connect1 = ConnectHandler(**device1)
print(net_connect1.find_prompt())
output = net_connect1.send_command("show ver")
print(output)

print("Disconnecting from device!")
net_connect1.disconnect()

net_connect2 = ConnectHandler(**device2)
print(net_connect2.find_prompt())
net_connect2.disconnect()

