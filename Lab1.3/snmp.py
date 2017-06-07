from pysnmp.hlapi import *






#snmp_object = ObjectIdentity ('SNMPv2-MIB','sysDescr',0)
#snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result1 = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107',161)),
                ContextData(),
                ObjectType(ObjectIdentity ('SNMPv2-MIB','sysDescr',0)))

result2 = nextCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107',161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False)



def snmp1(result1):
    for x in (result1):
        for y in x[3]:
            print(y)

def snmp2(result2):
    for x in (result2):
        for y in x[3]:
            print(y)


snmp1(result1)
print(" ")
snmp2(result2)
