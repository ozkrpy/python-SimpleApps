#!/usr/bin/env python3

import os
import sys


# f = open('/oracle/csv_generados/dwh/segmentador/dwh-segmentador.out','r') 
# Lines = f.readlines() 

# count = -1
# for line in Lines: 
#     print(line.lstrip(' ').replace('.','\t').rstrip('\n').upper())
# f.close()


with open(sys.argv[1], mode='r') as in_file, \
    open(sys.argv[2], mode='w') as out_file:
    for line in in_file: 
        linea_nueva=line.lstrip(' ').replace('.','\t').rstrip('\n').upper()
        print(linea_nueva)
        out_file.write(linea_nueva + '\n')