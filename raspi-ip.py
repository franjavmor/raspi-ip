import os

def raspi_ip():
    ipaddress = os.popen("hostname -I").readline()
    ipaddress = ipaddress.replace('\n', ' ').replace('\r', '')
    return ipaddress

print(raspi_ip())
