lista=[]
tope=999
cadena=''

def cargar_lista(texto: str, contador: int):
    global tope
    if (contador<=tope):
        #lista.append("'"+texto+"',")
        lista.append(texto)
    else:
        #tista.append(")"+'\n'+"AND('"+texto+"',")
        #tope+=1000
        lista.append('\n'+texto)
        tope+=1000
    
def remover_ultima_coma():
    item = lista[-1]
    item = item[:-1]+')'
    lista[-1]=item

def escribe_resultado(cadena: str):
    tope=2300
    while(len(cadena)>tope):
        # print('linea de texto mayor a:', str(tope))
        post=cadena[tope:]
        intro=post.find("','")+tope
        temporal=cadena[:intro+2]+'\n'+cadena[intro+2:]
        cadena=temporal
        tope+=2300
    # print(cadena)
    with open('resultado.txt', mode='w+') as resultado:
        resultado.write(cadena[:-1])
    
def main():   
    global tope
    global cadena
    with open('texto_a_procesar.txt', mode='r') as texto_plano:
        for c, linea in enumerate(texto_plano):
            #print(c, end='\r')
            #print(c, tope)
            #cargar_lista(linea.rstrip(), c)
            if (len(linea)>1):
                cadena = cadena + "'" + linea.rstrip() + "',"
                if (c>tope):
                    #escribe_resultado(cadena)
                    #lista.append(cadena)
                    cadena=cadena+'\n'
                    tope+=1000
    escribe_resultado(cadena.upper())  
        #remover_ultima_coma()
    

if __name__ == "__main__":
    main()