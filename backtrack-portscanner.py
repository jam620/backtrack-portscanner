#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket
from socket import *

#if __name__ == 'main':

equipo = input("Ingresa el dominio o ip que deseas escanear\n")
ip = gethostbyname(equipo)
print("Comenzando el escaneo en {}".format(ip))

for puertos in range(1, 1024):
    cliente = socket(AF_INET, SOCK_STREAM)
    resultado = cliente.connect_ex((equipo, puertos))
    if resultado == 0:
        print("Puerto %d: Abierto" % puertos)
        cliente.close()
    else:
        print('Puerto --->', puertos, "Cerrado o Filtrado")
