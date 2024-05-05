import socket
import psutil
import ipaddress

from pysnmp.entity.engine import SnmpEngine
from pysnmp.hlapi import getCmd, CommunityData, UdpTransportTarget, ContextData
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity

from portscanner import PortScanner


class snmp_scanner:


    def snmp_scanner(self):
        ips = PortScanner.ips_check(PortScanner.create_ip_list())
        community_string = "public"
        snmp_port = 161

        for ip in ips:
            try:
                errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(),
                                                                                 CommunityData(community_string),
                                                                                 UdpTransportTarget((ip,snmp_port)),
                                                                                 ContextData(),
                                                                                 ObjectType(ObjectIdentity("SNMPv2-MIB","sysDescr",0))
                                                                                 )
                                                                          )

                if errorIndication:
                    print('SNMP error:', errorIndication)
                elif errorStatus:
                    print(f'Error in SNMP response: {errorStatus} at {errorIndex}')
                else:
                    # Print results
                    for varBind in varBinds:
                        print(f'{varBind[0]} = {varBind[1]}')


            except errorIndication as  e:
                print(f'Error: {e}')


