#!/usr/bin/python3
from socket import gethostname, gethostbyname

ip = gethostbyname(gethostname())

with open('./.env', 'w') as e:
    e.write(f'IP_ADDR={ip}')
e.close()
