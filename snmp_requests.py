import pysnmp.entity.engine
from pysnmp.hlapi import CommunityData, UdpTransportTarget, getCmd, ContextData, nextCmd
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity


def get_request(oid, ip, port, com):
    engine = pysnmp.entity.engine.SnmpEngine()
    community = CommunityData(com)
    connection = UdpTransportTarget((ip, port))

    response = None
    err_ind = None
    err_stat = None

    try:
        var_bind = ObjectType(ObjectIdentity(oid))
        err_ind, err_stat, err_ind, response = next(
            getCmd(engine, community, connection, ContextData(), var_bind))
    except Exception as e:
        print(e)

    if err_ind:
        print(f"SNMP Hatası: {err_ind}")
        return None
    elif err_stat:
        print(f"SNMP Hatası: {err_stat.prettyPrint()}")
        return None
    if len(response) != 0:
        return response[0]
    else:
        return 0


def get_next_request(oid, ip, port, com):


    engine = pysnmp.entity.engine.SnmpEngine()
    community = CommunityData(com)
    connection = UdpTransportTarget((ip, port))

    err_ind = None
    err_stat = None
    response = None

    try:
        var_bind = ObjectType(ObjectIdentity(oid))
        err_ind, err_stat, err_ind, response = next(
            nextCmd(engine, community, connection, ContextData(), var_bind,    lookupMib=True, lookupValues=True))
    except Exception as e:
        print(e)

    if err_ind:
        print(f"SNMP Hatası: {err_ind}")
        return None
    elif err_stat:
        print(f"SNMP Hatası: {err_stat.prettyPrint()}")
        return None
    if response is not None:
        return response
    else:
        return 0
