import re
import utilidades

reRGB = re.compile(r'^#([A-F]|\d){6}$')
reHSL = re.compile(r'^hsl\((\d|[1-9]\d|[1-2]\d\d|3[0-5]\d|360)( *, *(\d|[1-9]\d|100)%){2}\)$')
reDirectorio = re.compile(r'^([A-Z]:|~|\.\.?)\\((\.\.|[a-zA-Z\d][^\\/:*?"><|]*)\\)*([a-zA-Z\d][a-zA-Z\d.]*\.[a-zA-Z\d.]*[a-zA-Z\d])$')
reCorreo = re.compile(r'^[a-zA-Z\d!#$%&’*+\-/=?^_‘{|}~]+(\.[a-zA-Z\d!#$%&’*+\-/=?^_‘{|}~]+)*@[a-zA-Z\d-]+(\.[a-zA-Z\d-]+)+$')
rePascal = re.compile(r'^{\d+( \d+)*}$')
reFecha = re.compile(r'^(\d{4})-(1[0-2]|0?[1-9])-(0?[1-9]|[1-2][0-9]|3[0-1])$')
#reXDSON = re.compile(r'^< *([a-zA-Z]+ *= *(\d+|(?P<comillas1>\"|\')[a-zA-Z\d]+(?P=comillas1)|\[ *(\d+|(?P<comillas2>\"|\')[a-zA-Z\d]+(?P=comillas2))( *, *(\d+|(?P<comillas3>\"|\')[a-zA-Z\d]+(?P=comillas3)))* *\]|(?P<candidato1><.*>)))( *, *([a-zA-Z]+ *= *(\d+|(?P<comillas4>\"|\')[a-zA-Z\d]+(?P=comillas4)|\[ *(\d+|(?P<comillas5>\"|\')[a-zA-Z\d]+(?P=comillas5))( *, *(\d+|(?P<comillas6>\"|\')[a-zA-Z\d]+(?P=comillas6)))* *\]|(?P<candidato2><.*>))))* *>$')
reXDSON = re.compile(r'^< *([a-zA-Z]+ *= *([1-9]\d*|(?P<comillas1>\"|\')[a-zA-Z\d]*(?P=comillas1)|\[ *(([1-9]\d*|(?P<comillas2>\"|\')[a-zA-Z\d]*(?P=comillas2))( *, *([1-9]\d*|(?P<comillas3>\"|\')[a-zA-Z\d]*(?P=comillas3)))*)? *\]|(?P<candidato1><.*>)))( *, *([a-zA-Z]+ *= *([1-9]\d*|(?P<comillas4>\"|\')[a-zA-Z\d]*(?P=comillas4)|\[ *(([1-9]\d*|(?P<comillas5>\"|\')[a-zA-Z\d]*(?P=comillas5))( *, *([1-9]\d*|(?P<comillas6>\"|\')[a-zA-Z\d]*(?P=comillas6)))*)? *\]|(?P<candidato2><.*>))))* *>$')
#xd = '< hola = 1 , joaoaoa = \"XDDDDDDDD\", tomc = 432, xdson = < holaestoydentro = 1 , yo = \"igual\">, M = [1,2,3,4]>'

lenguaje = []
palabras = open('palabras.txt', 'r')
for palabra in palabras:
    if reRGB.match(palabra) != None:
        lenguaje.append('RGB')
        continue

    if reHSL.match(palabra) != None:
        lenguaje.append('HSL')
        continue

    if reDirectorio.match(palabra) != None:
        lenguaje.append('Directorio')
        continue

    if reCorreo.match(palabra) != None:
        lenguaje.append('Correo')
        continue
    
    if rePascal.match(palabra) != None:
        nivel = list(map(int, re.findall(r'\d+', palabra)))
        if nivel == utilidades.pascalNivel(len(nivel)):
            lenguaje.append('Pascal')
        else:
            lenguaje.append('No pertenece al lenguaje')
        continue

    if reFecha.match(palabra) != None:
        if utilidades.fechaValida(*map(int, re.findall(r'\d+', palabra))):
            lenguaje.append('Fecha')
        else:
            lenguaje.append('No pertenece al lenguaje')
        continue

    if utilidades.matchRecursivo(palabra, reXDSON, ['candidato1', 'candidato2']):
        lenguaje.append('XDSON')
        continue

    lenguaje.append('No pertenece al lenguaje')
print('\n'.join(lenguaje))