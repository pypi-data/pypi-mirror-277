import nmap         # Import the Nmap Python module

def netdev_scan(ip):
    """
    Scan ports on the given IP address using Nmap.
    """
    nm = nmap.PortScanner()         # Create an instance of the Nmap PortScanner
    nm.scan(ip, '1-1024')       # Scan the specified IP address for open ports in the range 1-1024
    ports = []      # Initialize an empty list to store port information

    for proto in nm[ip].all_protocols():            # Loop through all protocols (usually 'tcp' and 'udp') found in the scan
        lport = nm[ip][proto].keys()        # Get all the port numbers for the current protocol
        for port in lport:          # Loop through each port and collect its state (open/closed)
            ports.append({
                'port': port,
                'state': nm[ip][proto][port]['state']
            })

    return ports        # Return the list of ports with their states

def netdev_detect_services(ip):
    """
    Detect services on the given IP address using Nmap.
    """
    nm = nmap.PortScanner()                 # Create an instance of the Nmap PortScanner
    nm.scan(ip, '1-1024', '-sV')                # Scan the specified IP address for open ports in the range 1-1024 and detect services and versions (-sV)
    services = []                   # Initialize an empty list to store service information

    for proto in nm[ip].all_protocols():        # Loop through all protocols (usually 'tcp' and 'udp') found in the scan
        lport = nm[ip][proto].keys()                # Get all the port numbers for the current protocol
        for port in lport:                  # Loop through each port and collect service details (state, name, product, version)
            services.append({
                'port': port,
                'state': nm[ip][proto][port]['state'],
                'name': nm[ip][proto][port]['name'],
                'product': nm[ip][proto][port]['product'],
                'version': nm[ip][proto][port]['version']
            })

    return services             # Return the list of services with their details


