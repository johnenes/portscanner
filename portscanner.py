import socket 
import termcolor 



def scan(target ,ports):
    print('\n' + 'Scanning The Target: ' + str(target))
    for port in range(1, ports): #looping through the supply number of port from 1 to the supply values
        scan_port(target, port) #scanning the target port


def scan_port(ipaddress,port):  #passing argument into the function
    try:
       sock  = socket.socket()# socket object initalization
       sock.connect((ipaddress,port))#connect target and ports
       print("[+] Port Open " + str(port))#concantenate the port into string
       sock.close()
 		  
    except:#check if the socket fails
       #print("[-] Port Closed " + str(port))  
        pass
 
targets  = input("[*] Enter Targets To Scan(split them by , ): ") 
ports    = int(input("[*] Enter How Many Port You Want to Scan: " ))


#check if there is comma , in the variable supply in the targets

if ',' in targets:
    print("[*] Scaning Multiple Targets")
    for ip_addr in targets.split(','): #looping throught the number of target ip address
        scan(ip_addr.strip(''), ports) # seperating the ip address by once completed
else:
    scan(targets,ports) #Scanning if only one ip address is proivded 
		 


	
 