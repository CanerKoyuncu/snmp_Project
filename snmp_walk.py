from file_ops import write_to_txt
from scannerclass import get_next_request, get_request


def start_snmpwalk(oid, ip, port, community):
    last_oid_data = []
    current_oid = oid
    oid_data = ["1"]
    data = [[[], []]]
    data[0][0].append(ip)
    data[0][0].append(community)
    data[0][0].append(port)
    while current_oid is not None and last_oid_data != oid_data:
        last_oid_data = oid_data
        oid_data = get_next_request(current_oid, ip, port, community)
        if oid_data is not None:
            current_oid = oid_data[0][0]
            if oid_data[0][1] != 0:
                data[0][1].append(oid_data[0])
            print(oid_data[0])
        elif oid_data is None:
            current_oid = str(current_oid[0:-1]) + str(int(current_oid[-1]) + 1)

    write_to_txt(ip, data)



if __name__ == '__main__':
    start_snmpwalk("1.3.6", "192.168.1.1", 161, "public")
    #var = get_request("1.3.6.1.2.1.2.2.1.4.6", "90.17.133.33", 161, "public")
    #print(var)
