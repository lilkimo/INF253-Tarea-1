def pascalNivel(nivel):
    coeficiente = 1
    numeros = []
    for iterador in range(1, nivel + 1):  
        numeros.append(coeficiente)
        coeficiente = int(coeficiente * (nivel - iterador) / iterador)
    return numeros

print(pascalNivel(11))