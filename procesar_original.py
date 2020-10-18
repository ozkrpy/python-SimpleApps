#!/usr/bin/env python3
import os, sys, stat 
import re

tns_conexion = 'dbadmin/Itagua15@dwh'

cadena_inicio: str='SET SERVEROUTPUT ON SIZE UNLIMITED\nSET HEADING OFF\nSET FEEDBACK OFF\nSET AUTOTRACE OFF\nSET LINESIZE 32767\nSET PAGESIZE 0\nSET TAB ON\nSET TERM OFF\nSET TRIMSPOOL ON\nSET TIME ON\nSET VERIFY OFF\nSET ARRAY 5000\nSET ESCCHAR $\nSET COLSEP "|"\nALTER SESSION SET NLS_DATE_FORMAT = "DD/MON/YYYY HH24:MI:SS"\n/\n'
cadena_fin: str='spool off\nEXIT\nEOFEOF\n'
    
def main():
    contador=0
    copiar_desde=0
    copiar_hasta=0
    print('Inicio.')
    try:
        archivo_entrada=open(sys.argv[1])
        for i, linea in enumerate(archivo_entrada):
            if ('spool') in linea:
                copiar_desde=i
                linea_temporal=" ".join(linea.split())
                nombre_archivo = re.split(r'/', linea_temporal)
                nombre_tabla = re.split(r'\.', nombre_archivo[5])
                continue
            if (chr(10)) in linea and (i == copiar_desde + 9):
                contador+=1
                copiar_hasta=i-1
                crear_archivo(str(contador)+'-'+nombre_tabla[1]+'.sql', copiar_desde, copiar_hasta)
            else:
                continue
    except Exception as e:
        print(e)
        archivo_entrada.close()

def crear_archivo(tabla_nombre: str, desde: int, hasta: int):
    nombre = tabla_nombre.replace('$','S')
    print('Generando:', nombre)#, end='\r')
    archivo_entrada=open(sys.argv[1],mode='r')
    archivo_salida=open(nombre, mode='w')
    archivo_salida.write(cadena_inicio)
    for i,line in enumerate(archivo_entrada):
        tope=2200
        linea_nueva=''
        if i >= desde and i <= hasta:
            linea_nueva = " ".join(line.split())
            if not (linea_nueva.startswith('select \'')):
                while (len(linea_nueva) > tope):
                    post=linea_nueva[tope:]
                    # intro=post.find("||'|'||")+tope #cuando se concatena
                    # intro=post.find(",")+tope #cuando se usa directo el nombre de columna
                    intro=post.find(", replace")+tope #cuando se usa directo el nombre de columna
                    if (intro==tope-1 or intro > (tope+200)):
                        # print('no se encontro replace')
                        intro=post.find(",")+tope
                    temporal=linea_nueva[:intro]+'\n       '+linea_nueva[intro:]
                    linea_nueva=temporal
                    tope=tope+2200
                    # if tope > 4800:
                    print('revisar el archivo:', nombre, 'lineas:', len(linea_nueva))
            archivo_salida.write(linea_nueva+'\n')
    archivo_salida.write(cadena_fin)
    archivo_entrada.close()
    archivo_salida.close()
    crear_shell(nombre)

def crear_shell(nombre: str):
    with open('shell_masivo.sh', mode='a') as shell_file:
        shell_file.write("echo '@"+nombre+" > Fecha: '`date '+%d/%m/%Y %H:%M:%S'`\nnohup sqlplus " + tns_conexion + " @"+nombre+" > /oracle/ejecuciones_script/"+nombre+".out 2>&1 &\n")
    os.chmod('shell_masivo.sh', stat.S_IRWXU)
    # print('Se genero el shell_masivo, y asigno el permiso de ejecucion.')

if __name__ == "__main__":
    main()