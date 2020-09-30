import re as regex

colores = '''
    #C4F407
    #ZZZZZZ
    Hello there!
    #F08
    45E097
    #FF00AA
    ...
'''
#print(regex.findall(r'(#(?:[A-F]|[0-9]){6}\b)', colores, regex.MULTILINE))
correos = '''
    guru99@google.com
    careerguru99@hotmail.com
    users@yahoo.com
'''
#print(regex.findall('[\w\.-]+@[\w\.-]+', correos, regex.MULTILINE))

# RGB
rgb = '#C4F407'
print(regex.search(r'^#([A-F]|[0-9]){6}$', rgb))

# HSL
hsl = 'hsl(900, 1% , 100%)'
print(regex.match(r'^hsl\((\d|[1-9]\d|[1-3]\d\d)( *, *(\d|[1-9]\d|100)%){2}\)$', hsl)) #Agregar un <= 360

# Directorio
directorio = 'E:\\Carpeta\\archivo.txt'
# Un directorio puede comenzar con '[A-Z]:\', '.\' o 'home ~\'. Adicionalmente, se puede partir haciendo referencia
# Al directorio padre '../', o con el padre del padre '../../', o el padre del padre del padre, etc...
# Por lo que esta sentencia es stackeable a diferencia de las otras tres opciones.
print(regex.match(r'^([A-Z]:\\|\.\\|~\\|(\.\.\\)+)([a-zA-Z0-9][^\\/:*?"><|]*\\)*([a-zA-Z0-9][a-zA-Z0-9.]*\.[a-zA-Z0-9.]*)$', directorio))

# Correo
correo = 'trivialito@ejemplo.correcto.com'
print(regex.search(r'[a-zA-Z0-9!#$%&’*+\-/=?^_‘{|}~](\.?[a-zA-Z0-9!#$%&’*+\-/=?^_‘{|}~])*', correo))

# Pascal
# ^{ \d+( \d+)* }$ <- Agregar enteros sin cero a la izquierda.
# ^{ (\d|[1-9]\d+)( (\d|[1-9]\d+))* }$ <- Revisar

# Fecha
fecha = '2020-02-29'
print(regex.search(r'[0-9]{4}(-[0-9]{1,2}){2}', correo))

# XDSON
xdson = ''
print(regex.search(r'< *([a-zA-Z]+ *= *([0-9]+|(\"|\')[a-zA-Z0-9]+\3|\[ *([0-9]+|(\"|\')[a-zA-Z0-9]+\5)( *, *([0-9]+|(\"|\')[a-zA-Z0-9]+\8))* *\]|(?R)))( *, *([a-zA-Z]+ *= *([0-9]+|(\"|\')[a-zA-Z0-9]+\12|\[ *([0-9]+|(\"|\')[a-zA-Z0-9]+\14)( *, *([0-9]+|(\"|\')[a-zA-Z0-9]+\17))* *\]|(?R))))* *>', xdson)
# ^-?([0-9]|[1-9][0-9]*)$// Enteros positivos y negativos sin 0 a la izquierda.
# ^-?(\d|[1-9]\d+)$// Enteros positivos y negativos sin 0 a la izquierda.
# (?P<xdson><.*>)