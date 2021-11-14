"""
checkValid.py file:
this file for checking validation input, and return results to the functions.py file
"""

import ipaddress
import re

"""
IsValid_IPv4_IPAddress function:
this function chek validation ipv4 address
"""
def IsValid_IPv4_IPAddress(ipv4Address):
    try:
        ipaddress.IPv4Network(ipv4Address)
        return ipv4Address
    except ValueError as e:
        return f"Error - {e}, is not a valid IPv4 Address"

"""
IsValid_IPv6_IPAddress function:
this function chek validation  ipv6 address 
"""
def IsValid_IPv6_IPAddress(ipv6Address):
    try:
        ipaddress.IPv6Network(ipv6Address)
        return ipv6Address
    except ValueError as e:
        return f"Error - {e}, is not a valid IPv6 Address"

"""
isValid_macAddress function:
this function chek validation Physical Address(mac Address)
"""
def isValid_macAddress(Physical_Address):
    macAdress = re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", Physical_Address.lower())
    if macAdress:
        return Physical_Address
    else:
        return f"Error - {Physical_Address}, is not a valid mac Address"
