import re
import utilidades

reRGB = re.compile(r'^#([A-F]|\d){6}$')
reHSL = re.compile(r'^hsl\((\d|[1-9]\d|[1-2]\d\d|3[0-5]\d|360)( *, *(\d|[1-9]\d|100)%){2}\)$')
reDirectorio = re.compile(r'^([A-Z]:|~|\.\.?)\\((\.\.|[a-zA-Z\d][^\\/:*?\"><|]*)\\)*([a-zA-Z\d][a-zA-Z\d.]*\.[a-zA-Z\d.]*[a-zA-Z\d])$')
reCorreo = re.compile(r'^[a-zA-Z\d!#$%&’*+\-/=?^_‘{|}~]+(\.[a-zA-Z\d!#$%&’*+\-/=?^_‘{|}~]+)*@[a-zA-Z\d-]+(\.[a-zA-Z\d-]+)+$')
rePascal = re.compile(r'^{(\d+(?: \d+)*)}$')
reFecha = re.compile(r'^(\d{4})-(1[0-2]|0?[1-9])-(0?[1-9]|[1-2][0-9]|3[0-1])$')
reXDSON = re.compile(r'^< *(?:(?:[a-zA-Z]+ *= *(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\1|\[ *(?:(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\2)(?: *, *(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\3))*)? *\]|(?P<candidato1><.*>)))(?: *, *(?:[a-zA-Z]+ *= *(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\5|\[ *(?:(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\6)(?: *, *(?:0|-?[1-9]\d*|(\"|\')[a-zA-Z\d]*\7))*)? *\]|(?P<candidato2><.*>))))*)? *>$')

palabras = open('palabras.txt', 'r')
for palabra in palabras:
    if reRGB.match(palabra) != None:
        print('RGB')
        continue

    if reHSL.match(palabra) != None:
        print('HSL')
        continue

    if reDirectorio.match(palabra) != None:
        print('Directorio')
        continue

    if reCorreo.match(palabra) != None:
        print('Correo')
        continue
    
    match = rePascal.match(palabra)
    if match != None:
        nivel = list(map(int, match.group(1).split(' ')))
        if nivel == utilidades.pascalNivel(len(nivel)):
            print('Pascal')
        else:
            print('No pertenece al lenguaje')
        continue

    match = reFecha.match(palabra)
    if  match != None:
        if utilidades.fechaValida(*map(int, match.groups())):
            print('Fecha')
        else:
            print('No pertenece al lenguaje')
        continue

    if utilidades.matchRecursivo(palabra, reXDSON, ['candidato1', 'candidato2']):
        print('XDSON')
        continue

    print('No pertenece al lenguaje')