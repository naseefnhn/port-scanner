# portscanner.py

import socket
import argparse
from datetime import datetime

def banner():
    print(r"""
    ***************************************
    *       Naseef's Port Scanner         *
    *   Fast and Simple Port Scanning     *
    ***************************************
    """)


def scan_host(ip, start_port, end_port):
    """Scan ports on a given IP."""
    print(f"[*] Scanning {ip} from port {start_port} to {end_port}")
    print(f"Start Time: {datetime.now()}\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Reduce timeout for faster scanning

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")

        sock.close()

    print(f"\nScan Completed at: {datetime.now()}")


def main():
    banner()

    parser = argparse.ArgumentParser(description="A simple port scanner tool by Naseef")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-sp", "--startport", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("-ep", "--endport", type=int, default=1024, help="End port (default: 1024)")

    args = parser.parse_args()

    scan_host(args.target, args.startport, args.endport)


if __name__ == "__main__":
    main()
