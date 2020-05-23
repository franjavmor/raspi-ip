import os

def raspi_ip():
    ipaddress = os.popen("hostname -I").readline()
    return ipaddress

print(raspi_ip())
