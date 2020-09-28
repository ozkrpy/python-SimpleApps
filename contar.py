#!/usr/bin/env python3
import sys
import re
from datetime import datetime, timedelta
import os

diccionario_db = {}
diccionario_archivo = {}


def main1():
    # captura el nombre del archivo DB que ingresa como argumento 1
    # el item 1 del objeto es el nombre de la base
    # el esquema se separa del . y el item 0 corresponde al nombre
    texto_nombre_db = re.split(r'-', str(sys.argv[1]).rstrip('\n'))
    base = texto_nombre_db[1]
    texto_esquema = re.split(r'\.', str(texto_nombre_db[2]).rstrip('\n'))
    esquema = texto_esquema[0]
    cargar_diccionario_db()
    cargar_diccionario_archivo()
    correctos, verificar, total = comparar_valores(base, esquema)
    print('                         ')
    print('TOTAL VERIFICADAS:', total)
    print('OK:', correctos)
    print('ERROR:', verificar)

def cargar_diccionario_db():
    global diccionario_db
    with open(sys.argv[1], mode='r') as base_datos:
        for tabla in base_datos:
            linea_tabla=re.split(r'\t', tabla)
            tabla_nombre=linea_tabla[0].rstrip('\n')
            cantidad_filas_tabla=linea_tabla[1].rstrip('\n')
            diccionario_db[tabla_nombre.lower()]=cantidad_filas_tabla

def cargar_diccionario_archivo():
    global diccionario_archivo
    with open(sys.argv[2], mode='r') as archivos:
        for archivo in archivos:
            linea_archivo=re.split(r'\s', archivo.lstrip(' '))
            nombre_tabla_archivo=re.split(r'\.', linea_archivo[1].rstrip('\n'))
            if (nombre_tabla_archivo[0] != 'total'):
                nombre_tabla=nombre_tabla_archivo[2]
                cantidad_filas_archivo=linea_archivo[0].rstrip('\n')
                diccionario_archivo[nombre_tabla.lower()]=cantidad_filas_archivo

def comparar_valores(base: str, esquema: str):
    global diccionario_archivo
    global diccionario_db   
    contadorOK=0
    contadorERROR=0
    d1_keys = set(diccionario_db.keys())
    d2_keys = set(diccionario_archivo.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    print ('TOTAL DE TABLAS:', len(d1_keys))
    print ('TOTAL DE LINEAS:', len(d2_keys))
    for tabla in shared_keys:
        if (diccionario_db[tabla] != 'ERROR_CONTEO'):
            lineas_archivo = int(diccionario_archivo[tabla])-1
            if (int(diccionario_db[tabla]) == lineas_archivo):
                agregar_registro(base, esquema, tabla+'\t'+diccionario_db[tabla]+'\t'+str(lineas_archivo)+'\tOK'+'\t'+base+esquema+'OK')
                contadorOK+=1
            else:
                agregar_registro(base, esquema, tabla+'\t'+diccionario_db[tabla]+'\t'+str(lineas_archivo)+'\tVERIFICAR'+'\t'+base+esquema+'VERIFICAR')
                contadorERROR+=1
        else:
            agregar_registro(base, esquema, tabla+'\t'+diccionario_db[tabla]+'\t'+str(lineas_archivo)+'\tERROR_CONTEO'+'\t'+base+esquema+'ERROR_CONTEO')
            contadorERROR+=1
        cantidad_tablas=contadorOK+contadorERROR
        print('EN PROCESO:', cantidad_tablas, end='\r')
    return contadorOK, contadorERROR, cantidad_tablas

def agregar_registro(base: str, esquema: str, cadena: str):
    with open('resumen.out', mode='a') as resumen:
        resumen.write(base+'\t'+esquema+'\t'+base+esquema+'\t'+cadena+'\n')

def main():
    print ('main')
    for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))

if __name__ == "__main__":
    print('*************************** INICIO ***************************')
    inicio = datetime.now()
    main()
    fin = datetime.now()
    intervalo = fin - inicio
    interval_minut0s = intervalo / timedelta(minutes=1)
    print('DURACION:', intervalo)
    print('*************************** FINAL ***************************')
    