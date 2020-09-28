#!/usr/bin/env python3

import os
import sys
from datetime import datetime

def main():
    contador = 0
    with open(sys.argv[1], mode='r') as in_file, \
        open(sys.argv[2], mode='w') as out_file:
        for line in in_file:
            linea_nueva = " ".join(line.split())
            out_file.write(linea_nueva + '\n')
            contador+=1
            print(contador, end='\r')
    print('TOTAL LINEAS:', contador)

try:
    inicio = datetime.now()
    print('Procesando: ', sys.argv[2], ', inicio: ', inicio.strftime("%d-%b-%Y (%H:%M:%S)"))
    main()
    final = datetime.now()
    intervalo = final - inicio
    print('Completado: ', sys.argv[2], ', Duracion: ', intervalo)
    
except Exception as e:
    print(e)