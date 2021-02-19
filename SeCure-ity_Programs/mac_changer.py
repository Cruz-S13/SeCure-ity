#!/usr/bin/env python3

#Kali Machine OG MAC_Add: 08:00:27:ec:30:a5
#Change to address:       00:11:22:33:44:55

#imports the subprocess module that allows you to use bash commands when called in the program.
import subprocess

user_conf = input("This program changes the MAC address of a specified target. Do you want to proceed (Yes/no)? ")

if user_conf == "no" or user_conf == "No" or user_conf == "NO" or user_conf == "":
    print("This operation will now end.")
elif user_conf == "Yes" or user_conf == "yes" or user_conf == "YES":
    t_interface = input("interface > ")
    n_mac = input("new MAC > ")
    print("[+] Changing MAC address for " + t_interface + " to " + n_mac)
    subprocess.call(["ifconfig", t_interface, "down"])
    subprocess.call(["ifconfig", t_interface, "hw", "ether", n_mac])
    subprocess.call(["ifconfig", t_interface, "up"])
else:
    print("Either you did not choose a valid selection, interface, or MAC address. This program will now end.")
