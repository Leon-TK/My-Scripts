import sys

import wakeonlan

# Wakes up a PC by WOL system
# CMD LINE ARGS. 1 - MAC address, 2 - ip address, 3 - port

if __name__ == "__main__":
    wakeonlan.send_magic_packet(sys.argv[1], ip_address = sys.argv[2], port = int(sys.argv[3]))