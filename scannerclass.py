import pysnmp.entity.engine
from pysnmp.hlapi import CommunityData, UdpTransportTarget, getCmd, ContextData, nextCmd, bulkCmd
from pysnmp.smi.rfc1902 import ObjectType, ObjectIdentity

import bulk_request
import file_ops


def snmp_scanner(ip_list):
    oids = file_ops.read_from_csv("files/oid.csv")
    for ip in ip_list:
        snmp_data = get_snmp_table(ip, oids)
        if snmp_data:
            file_ops.write_to_txt(f"files/{ip}.txt", snmp_data)


def get_snmp_table(ip, oids, com="public", port=161):

    data = []
    for oid in oids:
        get_response = get_request(oid[0], ip, port, com)
        if get_response != 0:
            oid = get_response[0]
            value = get_response[1]
            data.append([oid.prettyPrint(), value.prettyPrint()])

        get_next_response = get_next_request(oid, ip, port, "public")
        if get_next_response != 0:
            oid = get_next_response[0]
            value = get_next_response[1]
            data.append([oid.prettyPrint(), value.prettyPrint()])
    unique_data=[]
    for element in data:
        if not element in unique_data:
            unique_data.append(element)
    return unique_data


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

    else:
        return response


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
            nextCmd(engine, community, connection, ContextData(), var_bind, lexicographicMode=False))
    except Exception as e:
        print(e)

    if err_ind:
        print(f"SNMP Hatası: {err_ind}")
        return None
    elif err_stat:
        print(f"SNMP Hatası: {err_stat.prettyPrint()}")
        return None
    else:
        return response
