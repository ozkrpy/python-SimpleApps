import csv
import re
from zipfile import ZipFile
'''
OBSERVACIONES:
Entrada: lee el archivo .zip (C:/User/Downloads) que es generado desde el Service Desk - BI, no hace falta que sea unzipeado. Debe contener el archivo 'Completo.csv'
Salida: genera un archivo resultado .csv, con delimitador ',' que incluye los campos: Nro. OC, tipo de operacion, sentencia completa y tabla afectada.
'''
# PATRON DE BUSQUEDA, AGRUPADO SEGUN LA DESCRIPCION: [0] Sentencia, [1] Tabla, [2] Limitantes
update = r'(UPDATE(.*?)SET(.*?);)'
delete = r'(DELETE.+FROM(.*?)WHERE(.*?);)'
insert = r'(INSERT.+INTO(.*?)\((.*?);)'

# ABRIR EL ARCHIVO PARA ESCRIBIR LAS SENTENCIAS RECUPERADAS.
def abrir_archivo_resultado():
    try:
        archivo_resultado = open("./data/Resultado.csv",'w+', encoding="latin-1") 
        archivo_resultado.write("OC,operacion,sentencia,tabla\n")
        return archivo_resultado
    except Exception as e:
        return False

# ESCRIBE EN EL ARCHIVO DE RESULTADO.
def escribir_archivo(linea):
    outfile.write(linea)

# FUNCION QUE SE ENCARGA DE LEER EL STRING Y OBTENER LAS SENTENCIAS SOLICITADAS.
def recorrer_cadena(oc, cadena_recorrer, modificacion, patron_regex):
    match=re.findall(patron_regex, cadena_recorrer.upper())
    for element in match:
        cadena_escribir = oc + ",\"" + modificacion + '\",\"' + element[0] + "\",\"" + element[1].strip() + '\"\n'
        escribir_archivo(cadena_escribir)

# BUSCAR Y EXTRAER EL ARCHIVO CSV DENTRO DEL .ZIP
try:
    zip_path = ZipFile('c:\\\\Users\\ruffineo\\Downloads\\SoporteJOPARAaCSV.zip', 'r') # debe ser el path donde se descargo el reporte del SD, no hace falta extraer.
    zip_file = zip_path.extract('Completo.csv', path='./data')
    ordenes_de_cambio = open("./data/Completo.csv", "r", encoding="latin-1")
except Exception as e:
    print("Error al abrir el archivo zippeado.")

# LEER EL ARCHIVO .CSV
try:
    csvReader = csv.reader(ordenes_de_cambio, delimiter=',', quotechar='"')
    header = next(csvReader)
except Exception as e:
    print("Error al leer el archivo CSV")

# SI SE ABRE CORRECTAMENTE EL ARCHIVO DE RESULTADO, QUE SIGA LA EJECUCION.
outfile = abrir_archivo_resultado()
if outfile:
    for row in csvReader:
        if (len(row) == 11):
            orden_cambio = dict()
            orden_cambio['Indice'] = row[0]
            orden_cambio['OC'] = row[1]
            orden_cambio['Sumario'] = row[2]
            orden_cambio['Detalles'] = row[3]
            orden_cambio['Solicitante'] = row[4]
            orden_cambio['Ticket'] = row[5]
            orden_cambio['Creado'] = row[6]
            orden_cambio['Implementador'] = row[7]
            orden_cambio['Ejecutado'] = row[8]
            orden_cambio['Dia'] = row[9]
            orden_cambio['HoraEjecucion'] = row[10]
        
        recorrer_cadena(orden_cambio['OC'], orden_cambio['Detalles'], "UPDATE", update)
        recorrer_cadena(orden_cambio['OC'], orden_cambio['Detalles'], "DELETE FROM", delete)
        recorrer_cadena(orden_cambio['OC'], orden_cambio['Detalles'], "INSERT INTO", insert)

    outfile.close()
    print("Ejecucion terminada.")
else:
    print("Error al abrir el archivo salida.")