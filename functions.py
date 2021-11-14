"""
Fuctions.py file:
this file for check validation and do some actions and return results to the main
"""

import os
import requests
import socket
from checkValid import *

"""
get_image function getting image url address and check if status code success,
Opened the image file Fang as writing in binary, and let us point to with f variable
"""
def get_image(url):
    response = requests.get(url)
    if 200 <= response.status_code <= 299:
        with open("a.png", 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False


"""
get_ipv4 function: 
we get the IPV4 by the os.popen command, and then we read line by line with readLines command we cut the ipv4 
and then we send them to a function for checking if its IPV4 if yes it will return the IPV4 else it will return Error 
"""
def get_ipv4():
    ip = os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv4 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
            break
    return IsValid_IPv4_IPAddress(output)


"""
get_ipv6 function: 
we get the IPV6 by the os.popen command, and then we read line by line with readLines command we cut the ipv6 
and then we send them to a function for checking if its IPV6 if yes it will return the IPV6 else it will return Error 
"""
def get_ipv6():
    ip = os.popen("ipconfig")
    for line in ip.readlines():
        if "IPv6 Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
            break
    return IsValid_IPv6_IPAddress(output)


"""
get_mac_address function:
we get the Physical Address by the os.popen command, and then we read line by line with readLines command we cut the Physical Address 
and then we send them to a function for checking if its Physical Address if yes it will return the Physical Address
 else it will return Error 
"""
def get_mac_address():
    ip = os.popen("ipconfig -all")
    for line in ip.readlines():
        if "Physical Address" in line:
            start = line.find(":")
            end = -1
            output = line[start + 2:end]
            break
    return isValid_macAddress(output)


"""
get_dns_ipAddress function:
this function check validation URL Address , and return the URL IP Address
"""
def get_dns_ipAddress(hostname):
    if "www." in hostname or ".co.il" in hostname or "." in hostname and len(hostname) != 0:
        ip = socket.gethostbyname(hostname)
        return ip
    else:
        return False
