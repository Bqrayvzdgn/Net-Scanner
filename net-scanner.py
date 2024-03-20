import scapy.all as scapy
import argparse

class Banners:
    ERROR = """
    ███████╗██████╗░██████╗░░█████╗░██████╗░██╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
    █████╗░░██████╔╝██████╔╝██║░░██║██████╔╝██║
    ██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗╚═╝
    ███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║██╗
    ╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝
    """

    LOGO = """
    ██████╗░░██████╗░██████╗░██████╗░███████╗██╗░░░██╗
    ██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
    ██████╦╝██║██╗██║██████╔╝██║░░██║█████╗░░╚██╗░██╔╝
    ██╔══██╗╚██████╔╝██╔══██╗██║░░██║██╔══╝░░░╚████╔╝░
    ██████╦╝░╚═██╔═╝░██║░░██║██████╔╝███████╗░░╚██╔╝░░
    ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
    """

def get_user_input():
    print(Banners.LOGO)
    parser = argparse.ArgumentParser(description="This application was developed by kenxzz.", usage="python net-scanner.py -i [IP Field]", epilog="[Important] You must have sudo privileges for Net scanner to work properly.!")
    parser.add_argument("-i","--ipaddress", dest="ip_address",help="Enter IP address.")
    
    (user_input,arguments) = parser.parse_args()
    
    if not user_input.ip_address:
        print(Banners.ERROR)
    
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    combined_packet = broadcast_packet/arp_request_packet
    
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    
    answered_list.summary()

user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)
