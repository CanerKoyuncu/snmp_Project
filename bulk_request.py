from pysnmp.entity.engine import SnmpEngine
from pysnmp.hlapi import CommunityData, ContextData, UdpTransportTarget, bulkCmd
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity


def get_bulk_request(oid,ip, port =161, com= "public"):

    engine = SnmpEngine()
    community = CommunityData(com,mpModel=1)
    connection = UdpTransportTarget((ip, port))
    obj = ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr"))

    errInd, errStt, errIndex, varBinds = next(bulkCmd(
            engine,
            community,
            connection,
            ContextData(),
            0,25,
            obj
        ))
    return varBinds


if __name__ == '__main__':

    data = get_bulk_request("1.3.6.1.2.1.1",ip="192.168.1.1")
    print(data)

