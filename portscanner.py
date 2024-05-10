
import ipaddress
import socket

import psutil


def ip_check(ip, port=161):
    global result

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.settimeout(0.1)

    try:
        result = sock.connect_ex((ip, port))
    except socket.error as error:
        print(error)

    if result == 0:
        sock.close()
        return True
    else:
        sock.close()
        return False


def create_ip_list():
    ip_address = socket.gethostbyname(socket.gethostname())
    netmask = None
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                netmask = addr.netmask
                break
        if netmask:
            break

    network = ipaddress.IPv4Network(ip_address, strict=False)
    return network


def ips_check(net):
    open_devices = []

    ip_range = list(net.hosts())
    for ip in ip_range:
        if ip_check(str(ip)):
            open_devices.append(ip)
        else:
            pass
    print(open_devices)
    return open_devices

if __name__ == '__main__':
    network = create_ip_list()
    ips_check(network)
    print (ip_check("192.168.1.2"))