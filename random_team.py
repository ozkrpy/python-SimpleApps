import random
from bottle import post, request, route, run, static_file

# lista = [1,2,3,4,5,6,7,8,9,0]
lista = {}
cantidad = 5

@route('/')
def server_static(filepath="home.html"):
    return static_file(filepath, root='./')

# @route('/')
# def index():
#     return template('<b>Hello mondo</b>')

def sortear():
    while len(lista)>=cantidad:
        equipo = random.sample(lista, cantidad)
        for i in equipo:
            lista.remove(i)
        print(equipo)
        print(lista)

def leer_lista():
    with open('jugadores.txt',mode='r') as listado:
        for i in listado:
            # lista.append(i[:-1])
            numero, nombre = i.partition(',')[::2]
            # print(numero, nombre)
            # lista.append({numero,nombre[:-1]})#, nombre)
            lista[numero]=nombre[:-1]

if __name__ == "__main__":
    print("INICIO")
    leer_lista()
    # cargar_lista()
    # print(len(lista))
    #  sortear()
    run(host='localhost', port=5000, debug=True)