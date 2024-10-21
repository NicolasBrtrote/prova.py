#solucao 1
def tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i]==lista[j]:
                return True
    return False

#Tempo:
#linha 3- 3.8
#linha 4- 0.5
#linha 5- 0.5
#linha 6- 0.4

#solucao 2
def tem_duplicados(lista):
    lista_ordenada=sorted(lista)
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i]==lista_ordenada[i+1]:
            return True
        return False

 #Tempo:0.088



#solucao 3
def tem_duplicados(lista):
    elementos_vistos=set()
    for elementos in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

#Tempo:0.082