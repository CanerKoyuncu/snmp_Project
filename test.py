import argparse
from scannerclass import *


def add_args(parser):
    parser.add_argument("-s","--snmp_req", help="test aaa")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snmp_req","-sr", nargs=1, type=str, help="Snmp scanner for only ONE ip address.")
    parser.add_argument("--scan_with_list", "-sl", nargs=1, type=str, help="Snmp scanner for multiple ip addresses.")

    args = parser.parse_args()

    if args.snmp_req or args.sr:
        snmp_scanner(args.snmp_req[0])




if __name__ == "__main__":
    main()
