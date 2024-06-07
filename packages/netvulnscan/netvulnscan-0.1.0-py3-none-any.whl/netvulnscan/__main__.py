from netdev_discovery import netdev_discovery       # Import the network discovery function from the netdev_discovery module
from netdev_scan import netdev_detect_services          # Import the service detection function from the netdev_scan module
from netdev_vuln import netdev_scan_vulnerabilities         # Import the vulnerability scanning function from the netdev_vuln module

# Define the main function that will execute the network scanning and vulnerability detection
def main():
    network = '192.168.1.0/24'          # Specify the network to scan (e.g., the 192.168.1.0/24 network)
    devices = netdev_discovery(network)     # Discover devices on the specified network

    for device in devices:          # Loop through the discovered devices
        print(f"Scanning {device['ip']}...")        # Print a message indicating which IP address is being scanned
        services = netdev_detect_services(device['ip'])     # Detect services running on the current device's IP address
        vulnerabilities = netdev_scan_vulnerabilities(device['ip'])     # Scan the current device's IP address for known vulnerabilities
        print(f"Services: {services}")                  # Print the detected services
        print(f"Vulnerabilities: {vulnerabilities}")    # Print the found vulnerabilities
        
if __name__ == "__main__":          # If this script is being run directly, execute the main function
    main()
