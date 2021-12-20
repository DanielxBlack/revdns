#!/usr/local/bin/python3.5

import socket
import ipaddress
import os

#clear terminal and display banner
os.system("clear")

print(" _____            _____  _   _  _____ ")
print("|  __ \          |  __ \| \ | |/ ____|")
print("| |__) |_____   _| |  | |  \| | (___  ")
print("|  _  // _ \ \ / / |  | | . ` |\___ \ ")
print("| | \ \  __/\ V /| |__| | |\  |____) |")
print("|_|  \_\___| \_/ |_____/|_| \_|_____/ ")
print("                                      ")
print("--------------------------------------")
print("      Quick Reverse DNS Lookup        ")
print("                By Me                 ")
print("  Just a simple tool I am working on. ")
print("--------------------------------------")



IPaddy = input("Enter an IP or range: ")

# User the ipaddress module to convert \24 to all 256 valid IPs.
netWerk = ipaddress.ip_network(IPaddy)

# for loop to do reverse dns lookup and print hostname.
for IPs in netWerk.hosts():
    try:
        IPs = str(IPs)
        dns_lookup = socket.gethostbyaddr(IPs)
        result = dns_lookup[0]
        print(IPs + " resolves to " + result + ".")

    # if no response, pass.
    except socket.herror:
        pass


# printing an error message for each non-resolved IP can get cluttered.
print("If you got no results, our reverse DNS lookups went unanswered.")
