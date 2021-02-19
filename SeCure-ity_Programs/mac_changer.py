#!/usr/bin/env python

#Kali Machine OG MAC_Add: 08:00:27:ec:30:a5
#Change to address:       00:11:22:33:44:55

#imports the subprocess module that allows you to use bash commands when called in the program.
import subprocess

user_conf = raw_input("This program changes the MAC address of a specified target. Do you want to proceed (Yes/no)? ")

if user_conf = "no"
    break;
    else
        t_interface = raw_input("interface > ")
        n_mac = raw_input("new MAC > ")
        print("[+] Changing MAC address for " + t_interface + " to " + n_mac)
        subprocess.call(["ifconfig", t_interface, "down"])
        subprocess.call(["ifconfig", t_interface, "hw", "ether", n_mac])
        subprocess.call(["ifconfig", t_interface, "up"])
    else
        break;


#Uncomment the following to revert the last change you made to your MAC address.
# print("You are reverting the last change you made to your MAC Address: "
#       "\nNetwork Interface: " + net_intface +
#       "\nNew MAC Address: " + orig_intface +
#       "\nOld MAC Address: " + new_intface)
#
# subprocess.call("ifconfig eth0 down", shell=True) #Takes interface back down
# subprocess.call("ifconfig eth0 hw ether 08:00:27:ec:30:a5", shell=True) #Changes the mac address of eth0 to the original
# subprocess.call("ifconfig eth0 up", shell=True) #Brings eth0 interface active
