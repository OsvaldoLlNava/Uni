def Leer_Credenciales(ruta):
    archivo = open(ruta, 'r')
    credenciales = []
    for linea in archivo:
        cadena = ''
        espacio = 0
        texto = str(linea).strip()
        for i in range(0,len(texto)):
            if texto[i] == ' ':
                espacio +=1
            if espacio == 1 and texto[i] != ' ':
                cadena += texto[i]
            
        credenciales.append(cadena)
    
    return credenciales