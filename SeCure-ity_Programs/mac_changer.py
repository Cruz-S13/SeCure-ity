#!/usr/bin/env python

#Kali Machine OG MAC_Add: 08:00:27:ec:30:a5
#Change to address:       00:11:22:33:44:55

#imports the subprocess module that allows you to use bash commands when called in the program.
import subprocess

#Receive input from the user on which network interface to use and change the MAC address
interface = input("interface > ")
new_mac = input("new MAC > ")

#Feedback confirming what the user input.
print("[+] Changing MAC address for " + t_interface + " to " + n_mac)

#Calling the subprocess module to perform the bash command: ifconfig <args>
subprocess.call(["ifconfig", t_interface, "down"])
subprocess.call(["ifconfig", t_interface, "hw", "ether", n_mac])
subprocess.call(["ifconfig", t_interface, "up"])
