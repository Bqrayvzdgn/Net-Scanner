import scapy.all as scapy
import optparse

class Banners:
    ERROR = """
    ▒█▀▀▀ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ █ 
    ▒█▀▀▀ ▒█▄▄▀ ▒█▄▄▀ ▒█░░▒█ ▒█▄▄▀ ▀ 
    ▒█▄▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█ ▄
    """

    LOGO = """
    ▒█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▄ ▒█▀▀▀ ▒█░░▒█ 
    ▒█▀▀▄ ▒█░▒█ ▒█▄▄▀ ▒█░▒█ ▒█▀▀▀ ░▒█▒█░ 
    ▒█▄▄█ ░▀▀█▄ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄ ░░▀▄▀░
    """

def get_user_input():
    parse_object = optparse.OptionParser(description="This application was developed by bqrdev.", usage="python net-scanner",)
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("You must specify the Target IP Field for the attack to start.")
    return user_input

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list, args )= scapy.srp(combined_packet, timeout=3)
    answered_list.summary()
    
if __name__ == "__main__":
    print(Banners.LOGO)
    user_ip_address = get_user_input()
    scan_my_network(user_ip_address.ip_address)
    print("\nExiting.")
else:
    print(Banners.ERROR)