import sys

''' Approach del pipe
-Usar LCS y olbtener así el substring en común más largo
-Descartar este substring de ambos strings originales para así obtener las diferencias
-Guardar posiciones de las coincidencias para así obtener matches entre diferencias
-Matchear diferencias y printearlas

'''

'''
-Encontrar directamente las diferencias y parar en cada coincidencia para así matchear correctamente
-Guardar diferencias para encontrar la minima cantidad de pares de substrings(dinamismo)

'''

# Recibe ambos string originales y encuentra el el subtring en común
# 
def CASE(palabra1, palabra2):
    lp1 = len(palabra1)
    lp2 = len(palabra2)

    if lp1 == 0 or lp2 == 0:
        return ""

    if palabra1[lp1-1] == palabra2[lp2-1]:
        return CASE(palabra1[:-1], palabra2[:-1]) + palabra1[lp1-1]

    else:
        r1 = CASE(palabra1, palabra2[:-1])
        r2 = CASE(palabra1[:-1], palabra2)

        if r1 > r2:
            return r1

        return r2


### Recible ambos strings originales, compara con el string en común y así lo descarta de los originales obteniendo
### los pares que se diferencian

def slice(p1, p2):
    cruces = []
    s = CASE(p1, p2) #GJAB
    posPrev = 0
    posPrev2 = 0

    for c in s: #G
        pos1 = p1.index(c) #1
        pos2 = p2.index(c) #0
        cruce = (p1[posPrev:pos1], p2[posPrev2:pos2])

        if cruce != ('', ''):
            cruces.append(cruce)
        p1 = p1[pos1+1:]
        p2 = p2[pos2+1:]

    if len(p1) > 0 and len(p2) > 0:
        cruce = (p1, p2)
        cruces.append(cruce)

    elif len(p1) > 0:
        cruce = (p1, '')
        cruces.append(cruce)

    elif len(p2) > 0:
        cruce = ('', p2)
        cruces.append(cruce)

    return cruces




def main():
    data = sys.stdin.readlines()

    cantidadComparaciones = data[0].strip()

    paresAComparar = []

    par = 0
    buffer = []

    for linea in data[1:]:
        largo, texto = linea.strip().split(maxsplit=1)
        buffer.append(texto)

        if par % 2 == 1:
            buffer = tuple(buffer)
            paresAComparar.append(buffer)
            buffer = []
        par += 1

    data = []
    data.append(cantidadComparaciones)

    for p1, p2 in paresAComparar:
        lista = slice(p1, p2)
        data.append(len(lista))
        for e1, e2 in lista:
            s = e1 + " " + e2
            data.append(s)

    for linea in data:
        linea = str(linea) + "\n"
        sys.stdout.write(linea)
    
    return

    
if __name__ == "__main__":
    main()