import argparse
import snmp_walk
from portscanner import create_ip_list


def main():
    parser = argparse.ArgumentParser("snmp_tool")
    parser.add_argument("-p", "--port", help="This argument using for change port (default=161).")
    parser.add_argument("-i", "--ip", help="This argument using for specific ip address snmp scanning.")
    parser.add_argument("-c", "--code", help="This argument for change the start oid code. (default= "
                                             "'1.3.6.1.2.1.1.2.0' ")
    parser.add_argument("-oN", "--output_name", help="Output file name argument.", required=True)
    parser.add_argument("-v", "--verbose", help="Verbose mode.", action="store_true")

    args = parser.parse_args()

    if args.ip:
        snmp_walk.snmp_scanner(ip_list= [args.ip], port=args.port, oid=args.code, file_name=args.output_name, verbose= args.verbose)
    else:
        ips = create_ip_list()
        snmp_walk.snmp_scanner(ip_list= ips, port=args.port, oid=args.code, file_name=args.output_name, verbose= args.verbose)


if __name__ == "__main__":
    main()
