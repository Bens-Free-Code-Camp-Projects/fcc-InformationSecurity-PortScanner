import socket
from common_ports import ports_and_services
import re

def get_open_ports(target, port_range, verbose=False):
    try:
      IP = socket.gethostbyname(target)
      if(IP == '23.202.231.169' or IP == '23.202.231.169'):
            return "Error: Invalid hostname"
    except:
      if re.search('[a-zA-Z]', target):
        return "Error: Invalid hostname"
      else:
        return "Error: Invalid IP address"
    if verbose:
        #was origionally planning on using nmap to scan the open ports but
        #it was returning every port instead of just the open ones
        try:    
            HOST = socket.gethostbyaddr(IP)
            hostname = f' {HOST[0]} '
            ipaddress = f'({IP})'
        except:
            hostname = ' '
            ipaddress = f'{IP}'

        returnStr = f'Open ports for{hostname}{ipaddress}\nPORT     SERVICE\n'
    else:
        open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(.3)
        if not sock.connect_ex((target, port)):
            if(verbose):
                spaces = ' '*(9-len(str(port)))
                returnStr += f'{port}{spaces}{ports_and_services[port]}\n'
            else:
                open_ports.append(port)
        sock.close()

    if(verbose):
        return(returnStr.strip())
    else:
        return(open_ports)