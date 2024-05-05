from snmp_scanner import snmp_scanner

if __name__ == '__main__':

   snmp = snmp_scanner.snmp_scanner("192.168.1.1")
   print(snmp)
