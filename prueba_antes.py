#Función que dice si un año es bisiesto, devuelve 1 si TRUE, 0 si FALSE
def bisiesto(anio):
    if anio % 4 != 0:
        return 0
    else:
        if anio%100 == 0:
            if anio%400 == 0:
                return 1
            else: return 0
        else: return 1

#Función que devuelve los días de un mes del año, teniendo en cuenta bisiestos
def cantdias(mes, anio):
    if mes in {1,3,5,7,8,10,12}:
        return 31
    elif mes in {4,6,9,11}:
        return 30
    elif mes == 2:
        return 28 + bisiesto(anio)


#Función que te devuelve que fecha es mayor entre 2 fechas
def mayor(fecha_1, fecha_2):
    dia_1, mes_1, anio_1 = map(int, fecha_1.split('-'))
    dia_2, mes_2, anio_2 = map(int, fecha_2.split('-'))
    fecha1 = dia_1 + mes_1*100 + anio_1*10000
    fecha2 = dia_2 + mes_2*100 + anio_2*10000
    if fecha1 > fecha2: 
        return 1
    elif fecha1 < fecha2:
        return 2
    else: return 3


#Función que te dice cuantos días hay entre 2 fechas
def separacion(fecha_1, fecha_2):
    dia_1, mes_1, anio_1 = map(int, fecha_1.split('-'))
    dia_2, mes_2, anio_2 = map(int, fecha_2.split('-'))
    
    #Dependiendo de que fecha es mayor ordenamos los arrays a conveniencia
    aux = mayor(fecha_1, fecha_2)
    if aux == 3:
        print('fecha 1 = fecha 2')
        return 0
    elif aux == 1:
        print('fecha 1 > fecha 2 ')
        fechas = [dia_1, dia_2, mes_1, mes_2, anio_1, anio_2]
    else: 
        fechas = [dia_2, dia_1, mes_2, mes_1, anio_2, anio_1]
        print('fecha 1 < fecha 2')

    #Calculamos los años, meses y dias de diferencia entre las fechas
    anio = fechas[4] - fechas[5]
    mes = fechas[2] - fechas[3]
    dia = fechas[0] - fechas[1]
    if dia < 0:
        mes -= 1
        dia = cantdias(fechas[2], fechas[4]) + dia

    if mes < 0:
        anio -= 1
        mes = 12 + mes

    x = 1
    tot = 0
    #calculamos la cantidad de días que hay entre los años de diferencia
    for i in range(fechas[5]+1, fechas[4]):
        tot += bisiesto(i) + 365
    #Calculamos los meses de diferencia que hay entre las 2 fechas
    for i in range(fechas[3]+1, fechas[2]):
        tot += cantdias(i, fechas[5])
    if fechas[5] == fechas[4]:
        igual = [fechas[2], fechas[3]]; x = 0
    else: igual = [13, 1]
    if fechas[3] != fechas[2]:
        tot += cantdias(fechas[3], fechas[5]) - fechas[1]
        tot += fechas[2]
        for i in range(igual[1], fechas[2]):
            tot += cantdias(i, fechas[4])
        for i in range(fechas[3]+1, igual[0]):
            tot += cantdias(i, fechas[5])

    else: tot = tot*x + (max(fechas[0],fechas[1]) - min(fechas[0],fechas[1]))

    return [tot, anio, mes, dia]

print('indique todas las fechas como DD-MM-YYYY')
fecha_1 = input('indique fecha 1: ')
fecha_2 = input('indique fecha 2: ')

resultado = separacion(fecha_1, fecha_2)

print(resultado[0], 'días de diferencia entre', 
      fecha_1, 'y', fecha_2)
print(resultado[1], 'años', resultado[2], 'meses',
      resultado[3], 'días de diferencia entre', 
      fecha_1, 'y', fecha_2)