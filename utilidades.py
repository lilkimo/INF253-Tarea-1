def pascalNivel(nivel):
    for linea in range(1, nivel + 1):  
        coeficiente = 1
        numeros = []
        for iterador in range(1, linea + 1):  
            numeros.append(coeficiente)
            coeficiente = int(coeficiente * (linea - iterador) / iterador) 
    return numeros

def fechaValida(ano, mes, dia):
    if not 0 < mes < 13:
        False

    if mes == 2:
        limite = 28
        if (ano%4 == 0 and (ano%100 != 0 or ano%400 == 0)):
            limite = 29
    else:
        limite = 31
        if (mes < 8 and mes%2 == 0) or (mes >= 8 and mes%2 != 0):
            limite = 30
    
    if dia > limite:
        return False
    return True

def matchRecursivo(string, regEx, candidatos):
    if string == None:
        return True
    
    match = regEx.match(string)
    if match == None:
        return False
    
    for candidato in candidatos:
        if matchRecursivo(match.group(candidato), regEx, candidatos) == False:
            return False
    return True