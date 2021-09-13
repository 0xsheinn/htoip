#!/usr/bin/python3
#sheinn
# I'm created this tools for changing all subdomains to ips at the same time and scan with masscan for open ports

import socket
import argparse
import sys

parser = argparse.ArgumentParser(description='Host to IP tool by sheinn')
parser.add_argument('-l','--list', help='url lists', required=True)
args = parser.parse_args()

urls = args.list

def host_to_ip(urls):
	print(f"IPs \t\t\t\t Hosts\n")
	with open(urls, "r") as hosts:
		for host in hosts:
			h = host.strip().replace("https://","").replace("http://","")
			ip = socket.gethostbyname(h)
			with open("host-to-ips.out","a") as ips:
				ips.write(ip + '\n')
			print(f"{ip} \t\t\t {h}")

if __name__ == "__main__":
	host_to_ip(urls)