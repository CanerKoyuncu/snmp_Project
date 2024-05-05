from socket import socket

import ipaddress
import psutil


class PortScanner():

    def __init__(self, port=161):
        self.port = port

    def ip_check(self, ip):
        global result
        sock = socket.socket(socket.AF_INET)
        sock.settimeout(0.1)

        try:
            result = sock.connect_ex((ip, self.port))
        except socket.error as error:
            print(error)

        if result == 0:
            sock.close()
            print(ip)
            return True
        else:
            sock.close()
            return False

    def create_ip_list(self):
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

    def ips_check(self, net):
        open_devices = []

        ip_range = list(net.hosts())
        for ip in ip_range:
            if(self.ip_check(str(ip))):
                open_devices.append(ip)
            else:
                pass

        return open_devices
