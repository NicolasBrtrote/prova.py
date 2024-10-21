from line_profiler import profile




@profile
def tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i]==lista[j]:
                return True
    return False
    
listateste = [1, 2, 3, 4, 5, 6, 3]
print(tem_duplicados(listateste))