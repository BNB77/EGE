from ipaddress import *

net = ip_network('192.168.2.0/255.255.254.0')

c = 0
for i in net:
    c += 1
    print(c - 2)
