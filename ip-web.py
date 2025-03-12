import socket

URL = input("link - - >")
ip = socket.gethostbyname(URL)
print("ip - - >" +ip)
print("Have a nice day") 
