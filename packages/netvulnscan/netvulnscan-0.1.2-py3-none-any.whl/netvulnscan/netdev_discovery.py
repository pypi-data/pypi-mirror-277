from scapy.all import ARP, Ether, srp           # Import necessary functions and classes from the Scapy library

def netdev_discovery(network):
    """
    Discover devices in the given network using ARP requests.
    """
    # Create an ARP request
    arp = ARP(pdst=network)         # Create an ARP request packet with the specified network
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")      # Create an Ethernet frame with the broadcast MAC address
    packet = ether/arp      # Combine the ARP request and Ethernet frame to form the complete packet

    result = srp(packet, timeout=3, verbose=0)[0]       # Send the packet on the network and wait for responses (timeout after 3 seconds, no verbose output)
    devices = []         # Initialize an empty list to store discovered devices

    for sent, received in result:       # Loop through the responses and extract the IP and MAC addresses of the responding devices
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices       # Return the list of discovered devices

