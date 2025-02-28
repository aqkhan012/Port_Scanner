import socket
import os


#func to ping the and checks whether the host is reachable or not



#assci Art
art = """

                                 /$$            /$$$$$$                                                             
                                | $$           /$$__  $$                                                            
  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$        | $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
 /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/        |  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \__/  | $$           \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  | $$| $$  | $$| $$        | $$ /$$       /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$/| $$        |  $$$$/      |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$      
| $$____/  \______/ |__/         \___/         \______/  \_______/ \_______/|__/  |__/|__/  |__/ \_______/|__/      
| $$                                                                                                                
| $$                                                                                                                
|__/                                                                                                                

BY >> Abdul Qadir \n
"""
print(art)


#user input
ip_input = input("Enter the IP address: ")
port_start = int(input("Enter the port number: "))
port_end = int(input('Enter An End port:'))


#Function to scan ip's and discover open ports
def port_discovery(ip_input,port_start,port_end):
    print('[+] scaning the target', ip_input)
    for port in range(port_start,port_end +1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((ip_input,port))
        if result == 0:
            print(f'[✔] port {port} is open')
        s.close()
port_discovery(ip_input,port_start,port_end) #calling function here
print('scan was completed')

import sys, time

def progress_bar(duration=5, length=30):
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = "#" * i + "-" * (length - i)
        sys.stdout.write(f"\r[{bar}] {percent}%") 
        sys.stdout.flush()
        time.sleep(duration / length)
    print("\n[✔] Completed!")

progress_bar(5)
