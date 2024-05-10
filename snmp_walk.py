import file_ops

from snmp_requests import get_next_request


def snmp_scanner(ip_list,file_name, port=161, com="public", oid="1.3.6.1.2.1.1.3.0", verbose= False):
    if oid == None:
        oid = "1.3.6.1.2.1.1.2.0"
    if port == None:
        port = 161
    if com == None:
        com = "public "
    for ip in ip_list:
        snmp_data = get_snmp_table(oid, ip, port, com, verbose)
        if snmp_data:
            file_ops.write_to_txt(f"{file_name}.txt", snmp_data)

def get_snmp_table(oid, ip, port, com,verbose):
    data = start_snmpwalk(oid, ip, port, com,verbose)
    unique_data = []
    for element in data:
        if element not in unique_data:
            unique_data.append(element)
    return unique_data


def start_snmpwalk(oid, ip, port, community, verbose):
    response_array = [[], []]
    response_array[0].append(ip)
    response_array[0].append(port)
    response_array[0].append(community)
    response_array[0].append(oid)
    current_oid = oid
    last_oid_data = 1
    oid_data = None
    while current_oid is not None and last_oid_data != oid_data:
        last_oid_data = oid_data
        oid_data = get_next_request(current_oid, ip, port, community)
        if oid_data != 0:
            current_oid = oid_data[0][0]
            response_array[1].append(oid_data)
            if verbose:
                print(oid_data[0].prettyPrint())
        else:
            return response_array
