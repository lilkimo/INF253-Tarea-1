'''
pascalNivel
-----------------------
nivel : int
------------------------
Retorna la fila número <nivel> del triangulo de pascal en forma de lista. Es decir,
si <nivel> = 1 entonces retornará [1], si <nivel> = 2 entonces [1, 1], etc...
'''
def pascalNivel(nivel):
    if nivel < 1:
        raise ValueError('El nivel indicado debe ser superior a 1')
    
    coeficiente = 1
    numeros = []
    for iterador in range(1, nivel + 1):  
        numeros.append(coeficiente)
        coeficiente = int(coeficiente * (nivel - iterador) / iterador)
    return numeros

'''
fechaValida
-----------------------
ano : int
mes : int
dia : int
------------------------
Retorna True sí es una fecha válida, False si es una fecha imposible.
'''
def fechaValida(ano, mes, dia):
    if not 0 < mes < 13:
        return False
    if dia < 1:
        return False
    if dia < 29:
        return True

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

'''
matchRecursivo
-----------------------
string : (str|None)
regEx : re.Pattern
candidatos : (int|str)[]
------------------------
Sean <candidatos> una lista de grupos pertenecientes al Patrón <regEx>, esta función
revisará si <regEx> tiene un match con <string>, y si es así, revisará las subcadenas
generadas por los grupos pertenecientes a <candidatos>, de forma recursiva.

Retornará True si toda la cadena <string> es válida (De acuerdo a <regEx>). En caso
contrario, si la propia cadena <string> o alguna de las subcadenas candidatas no son
válidas, retornará False.
'''
def matchRecursivo(string, regEx, candidatos):
    for candidato in candidatos:
        if candidato not in regEx.groupindex:
            raise ValueError(candidato + ' no es un grupo perteneciente a ' + regEx.pattern)
    
    if string == None:
        return True
    
    match = regEx.match(string)
    if match == None:
        return False
    
    for candidato in candidatos:
        if matchRecursivo(match.group(candidato), regEx, candidatos) == False:
            return False
    return True