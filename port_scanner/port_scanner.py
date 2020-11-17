import socket
from common_ports import ports_and_services as port_list

def numeric_ip(str):
  return all(i.isnumeric() for i in str.split('.'))#SPLITS IP ADDRESS INTO NUMBERS TO CHECK IF THE STRING PASSED HAS NUMBERS 

def get_open_ports(target, port_range, verbose=False):#THIRD ARG OPTIONAL
  open_ports = [] #EMPTY LIST TO STORE OPEN PORTS
  try:
    ip_addr = socket.gethostbyname(target)#Retreives HOST IP Address
  except: #Check if arguments passed are valid IP addresses
    if numeric_ip(target):
      return "Error: Invalid IP address"
    else:
      return "Error: Invalid hostname"
    
  if not numeric_ip(target):
    hostname = target
  else:
    try:
      hostname = socket.gethostbyaddr(target)[0]#Gets the first value from the tuple returned
    except:
      hostname = False

  for port in range(port_range[0],port_range[1]+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.25)

    if(s.connect_ex((target, port))== 0): #connect_ex returns Error instead of raising Exception
      open_ports.append(port)
    s.close()

  if verbose==True: #IF THIRD ARGUMENT IS PASSED
    output = f"Open ports for "
    output += f"{hostname} ({ip_addr})\n" if hostname else f"{ip_addr}\n"
    output +=  "PORT     SERVICE\n"

    for port in open_ports:
      service = port_list[port]
      gap = 9 - len(str(port)) #TO DISPLAY VALUES RIGHT BELOW THE PORT AND SERVICE HEADER
      output+= f"{port}{' ' *gap}{service}"
      if port != open_ports[-1]:
        output += "\n"
    return output
  else:
    return open_ports