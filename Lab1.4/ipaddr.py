from ipaddress import IPv4Network
import random


class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        netip = random.randint(0x0B000000, 0xDF000000)
        netmask = random.randint(8, 24)
        IPv4Network.__init__(self,(netip,netmask),strict=False)

    def key_value(self):
        return int(self.network_address._ip) + (int(self.netmask._ip))

list = []
i=1
while (i<100):
    list.append(IPv4RandomNetwork())
    i+=1
for i in range(0,50):
    print(list)







