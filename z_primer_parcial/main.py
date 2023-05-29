import json
import csv
import re

def abrir_json(nombre_archivo:str):
    """
    recibe por parametro un string que indicara el nombre del archivo
    abre un archivo Json y lo convierte en una lista
    devuelve una lista con lo que hay dentro de ["jugadores"]

    """
    with open(nombre_archivo,"r") as archivo:
        data = json.load(archivo)
        data_lista = data["jugadores"]
    return data_lista


def listar_jugadores_posicion(lista:list):
    """
    recibe por parametro una lista
    comprueba que la lista tenga al menos un elemento y genera un mensaje con el nombre y la posicion
    devuelve una lista con los mensajes generados que contienen el nombre y posicion de cada jugador
    """
    lista_posicion = []
    if len(lista) > 0:
        for jugador in lista:
            jugador_listado = "{0} - {1}".format(jugador["nombre"],jugador["posicion"])
            lista_posicion.append(jugador_listado)
    else:
        print("No hay jugadores en esa lista")
    return lista_posicion

def listar_jugadores_indice(lista:list):
    """
    recibe por parametro una lista
    comprueba que la lista tenga al menos un elemento y genera un mensaje con el nombre y el indice del mismo
    no devuelve nada, pero imprime por pantalla un mensaje con los jugadores y sus indices
    """
    if len(lista) > 0:
        for jugador in range(len(lista)):
            print("{0} - {1}".format(lista[jugador]["nombre"],jugador))
    else:
        print("No hay jugadores en esa lista")

def estadisticas_completas_por_jugador(lista:list):
    """
    recibe por parametro una lista
    imprime la funcion que hace una lista por indices, luego pregunta al usuario el indice del jugador y guarda en una nueva lista
    devuelve la lista con el nombre, la posicion y las estadisticas
    """
    print(listar_jugadores_indice(lista_dream_team))
    jugador_seleccionado = []
    condicion_flag = True
    while(condicion_flag == True):
        opcion_indice = int(input("Que indice de jugador deseas ingresar?: "))
        if opcion_indice < len(lista):
            condicion_flag = False
        else:
            print("Numero de indice no valido\n")

    for jugador in range(len(lista)):
        if jugador == opcion_indice:
            jugador_seleccionado.append(lista[opcion_indice]["nombre"])
            jugador_seleccionado.append(lista[opcion_indice]["estadisticas"])
            jugador_seleccionado.append(lista[opcion_indice]["posicion"])

    return jugador_seleccionado


def calcular_promedio_equipo(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a buscar
    comprueba que la liste no este vacia, despues acumula y cuenta dentro de las estadisticas del jugador el dato pedido, con eso saca el promedio
    devuelve el promedio del dato pasado por parametro de la lista
    """
    contador = 0
    acumulador = 0
    if len(lista) > 0:
        for jugador in range(len(lista)):
            acumulador += float(lista[jugador]["estadisticas"][dato])
            contador += 1
    
    promedio = acumulador/contador
    return promedio

def ordenamiento_por_nombre(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a comparar
    comprueba que la lista no este vacia, y ordena a los jugadores de manera descendente agregando los nombres de cada uno en una nueva lista
    devuelve la nueva lista con los nombres de los jugadores ordenados
    """
    lista_ordenada = []
    if len(lista) <= 1:
        return lista
    else:
        cantidad_lista = len(lista)
        for i in range(cantidad_lista):
            for j in range(cantidad_lista - i - 1):
                if lista[j]["estadisticas"][dato] < lista[j+1]["estadisticas"][dato]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        for jugador in lista:
            lista_ordenada.append(jugador["nombre"])

    return lista_ordenada

def ordenamiento(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a comparar
    comprueba que la lista no este vacia, y ordena a los jugadores de manera descendente agregando los jugadores en una nueva lista
    devuelve la nueva lista con todos los datos de los jugadores ordenados
    """
    lista_ordenada = []
    if len(lista) == 1:
        return lista
    else:
        cantidad_lista = len(lista)
        for i in range(cantidad_lista):
            for j in range(cantidad_lista - i - 1):
                if lista[j]["estadisticas"][dato] < lista[j+1]["estadisticas"][dato]:
                    lista[j],lista[j+1] = lista[j+1],lista[j]
        for jugador in lista:
            lista_ordenada.append(jugador)

    return lista_ordenada

def calcular_mostrar_mayor_dato(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a comparar
    comprueba que la liste no este vacia y calcula el jugador que tenga la mayor cantidad del dato pedido, tambien comprueba si alguien tiene la misma cantidad del mayor dato
    devuelve un mensaje que imprime por pantalla el o los nombres de las personas con mayor cantidad y el dato pedido
    """
    maximos_iguales = 0
    if len(lista) > 1:
        indice_max = 0
        maximos = 0
        for jugador in range(len(lista)):
            if indice_max == 0 or lista[jugador]["estadisticas"][dato] > maximos:
                maximos = lista[jugador]["estadisticas"][dato]
                indice_max = jugador
            elif lista[jugador]["estadisticas"][dato] == maximos:
                maximos_iguales = lista[jugador]["estadisticas"][dato]
                indices_max_iguales = jugador
    else:
        return lista
    
    if maximos_iguales == maximos:
        maximo_dato = print("Los maximos en la estadistica {0} son {1} y {3} con una cantidad de {2}".format(dato,lista[indice_max]["nombre"],maximos,lista[indices_max_iguales]["nombre"]))
    else:
        maximo_dato = print("El maximo en la estadistica {0} es {1} con una cantidad de {2}".format(dato,lista[indice_max]["nombre"],maximos))

    return maximo_dato

def mayor_al_dato_ingresado_nombres(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a comparar
    le pide al usuario un numero y compara ese numero con las estadisticas del jugador, generando una nueva lista con los nombres de los jugadores que superen el numero pedido
    devuelve una lista con los nombres de los jugadores que superen el numero ingresado por el usario en el dato deseado
    """
    valor_ingresado = float(input("Ingrese un valor para mostrar que jugadores superan en {0}: ".format(dato)))
    lista_mayor_al_valor = []
    for jugador in lista:
        if jugador["estadisticas"][dato] > valor_ingresado:
            lista_mayor_al_valor.append(jugador["nombre"])

    if len(lista_mayor_al_valor) == 0:
        return("No hay jugadores que superen el dato ingresado")

    return lista_mayor_al_valor

def mayor_al_dato_ingresado_posicion(lista:list, dato:str):
    """
    recibe dos parametros una lista y un string que representa el dato a comparar
    le pide al usuario un numero y compara ese numero con las estadisticas del jugador, generando una nueva lista con los nombres y posicion de los jugadores que superen el numero pedido
    devuelve una lista con los nombres y posicion de los jugadores que superen el numero ingresado por el usario en el dato deseado
    """
    valor_ingresado = float(input("Ingrese un valor para mostrar que jugadores superan en {0}: ".format(dato)))
    lista_mayor_al_valor = []
    for jugador in lista:
        if jugador["estadisticas"][dato] > valor_ingresado:
            lista_mayor_al_valor.append(jugador)

    if len(lista_mayor_al_valor) == 0:
        return("No hay jugadores que superen el dato ingresado")

    return lista_mayor_al_valor

def calcular_mostrar_mayor_logro(lista:list):
    """
    recibe una lista como parametro
    comprueba que la lista no este vacia y calcula que jugador tiene mas cantidad de logros individuales diferentes, no acumulan la cantidad de logros repetidos
    devuelve un mensaje que indica que jugador es el que tiene mas logros y cuantos logros
    """
    largo_lista =  len(lista)
    if largo_lista <= 1:
        return lista
    else:
        for jugador in range(largo_lista):
            if jugador == 0 or len(lista[jugador]["logros"]) > cant_logros:
                cant_logros = len(lista[jugador]["logros"])
                mensaje = "El jugador con mayor cantidad de logros es {0} con {1} logros diferentes:\n{2}".format(lista[jugador]["nombre"],cant_logros,lista[jugador]["logros"])

    return mensaje


def buscador_por_nombre_mostrar_logros(lista:list):
    """
    recibe por parametro una lista
    le pide al usuario un nombre y compara el nombre con los de la lista
    devuelve un mensaje indicando si el jugador existe o no y si existe devuelve el nombre y sus logros
    """
    nombre_buscado = input("Ingrese el nombre a buscar: ").lower()
    for jugador in lista:
        if nombre_buscado == jugador["nombre"].lower():
            mensaje = "El jugador {0} tiene los siguientes logros: {1}".format(nombre_buscado.title(), jugador["logros"])
            break
        else:
            mensaje = "No existe jugador con ese nombre"

    return mensaje

def buscador_por_nombre_mostrar_logros(lista:list):
    """
    recibe por parametro una lista
    le pide al usuario un nombre y compara el nombre con los de la lista
    devuelve un mensaje indicando si el jugador existe o no y si existe devuelve el nombre y sus logros
    """
    nombre_buscado = input("Ingrese el nombre a buscar: ").lower()
    for jugador in lista:
        if nombre_buscado == jugador["nombre"].lower():
            logros = jugador["logros"]
            break
        else:
            logros = "No existe jugador con ese nombre"
    
    return logros

def pertenece_salon_fama(lista:list):
    """
    recibe por parametro una lista
    utiliza la funcion buscador_por_nombre_mostrar_logros(lista:list) y genera una lista de los logros del jugador, compara el string si pertenece al salon de la fama o no
    devuelve un mensaje indicando si pertenece o no al salon de la fama
    """
    lista_logros_jugador = buscador_por_nombre_mostrar_logros(lista)
    if "Miembro del Salon de la Fama del Baloncesto" in lista_logros_jugador:
        mensaje = print("El jugador pertenece al salon de la fama")
    else:
        mensaje = print("El jugador no pertenece al salon de la fama")
    
    return mensaje




lista_dream_team = abrir_json("z_primer_parcial/dt.json")
contador_caso_2 = 0
while True:
    opcion = input("\n1 - Mostrar la lista de todos los jugadores del Dream Team\n2 - Mostrar estadísticas completas por indice\n3 - Permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.\n4 - buscar un jugador por su nombre y mostrar sus logros\n5 - Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.\n6 - Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n7 - Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n8 - Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n9 - Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n10 - Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n11 - Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n12 - Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n13 - Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n14 - Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n15 - Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor. \n16 - Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n17 - Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos\n18 - Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n19 - Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas\n20 - Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.\n23 -  Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking(ptos,reb,asis,rob)\n0 - SALIR \nSeleccione su opcion: ")
    match(opcion):
        case "1":
            lista_jugador_posicion = listar_jugadores_posicion(lista_dream_team)
            for jugador in lista_jugador_posicion:
                print(jugador)
        case "2":
            jugador_con_estadisticas = estadisticas_completas_por_jugador(lista_dream_team)
            contador_caso_2 =+ 1

        case "3":
            if contador_caso_2 > 0:
                dict_est = jugador_con_estadisticas[1]
                solo_nomb = jugador_con_estadisticas[0]
                solo_pos = jugador_con_estadisticas[2]
                columnas_titulo = ""
                columnas_valor = ""
                for campo in dict_est:
                    columnas = "{0},".format(campo)
                    columnas_titulo = columnas_titulo + columnas
                    valor_columnas = "{0},".format(dict_est[campo])
                    columnas_valor = columnas_valor + valor_columnas
                guardar_final = "nombre,posicion,{0}".format(columnas_titulo[:-1])
                guardar_final_est = "{0},{1},{2}".format(solo_nomb,solo_pos,columnas_valor[:-1])
                with open ("stat_jugador.csv","w") as archivo:
                    archivo.write(guardar_final)
                    archivo.write("\n")
                    archivo.write(guardar_final_est)
            else:
                print("No ingreso al caso 2 para seleccionar un jugador")
        case "4":
            print(buscador_por_nombre_mostrar_logros(lista_dream_team))
        case "5":
            promedio_puntos = calcular_promedio_equipo(lista_dream_team, "promedio_puntos_por_partido")
            print("El promedio de puntos del dream team es: {0}".format(promedio_puntos))
            print(ordenamiento_por_nombre(lista_dream_team,"promedio_puntos_por_partido"))
        case "6":
            pertenece_salon_fama(lista_dream_team)
        case "7":
            calcular_mostrar_mayor_dato(lista_dream_team,"rebotes_totales")
        case "8":
            calcular_mostrar_mayor_dato(lista_dream_team,"porcentaje_tiros_de_campo")
        case "9":
            calcular_mostrar_mayor_dato(lista_dream_team,"asistencias_totales")
        case "10":
            print(mayor_al_dato_ingresado_nombres(lista_dream_team,"promedio_puntos_por_partido"))
        case "11":
            print(mayor_al_dato_ingresado_nombres(lista_dream_team,"promedio_rebotes_por_partido"))
        case "12":
            print(mayor_al_dato_ingresado_nombres(lista_dream_team,"promedio_asistencias_por_partido"))
        case "13":
            calcular_mostrar_mayor_dato(lista_dream_team,"robos_totales")
        case "14":
            calcular_mostrar_mayor_dato(lista_dream_team,"bloqueos_totales")
        case "15":
            print(mayor_al_dato_ingresado_nombres(lista_dream_team,"porcentaje_tiros_libres"))
        case "16":
            lista_ppp = ordenamiento(lista_dream_team,"promedio_puntos_por_partido")
            lista_sin_peor = lista_ppp[:-1]
            promedio_sin_peor = calcular_promedio_equipo(lista_sin_peor,"promedio_puntos_por_partido")
            print("\nEl promedio de puntos por partido sacando al peor promedio es: {0}".format(promedio_sin_peor))
            print("Siendo el peor {0} con {1} puntos por partido".format(lista_ppp[-1]["nombre"],lista_ppp[-1]["estadisticas"]["promedio_puntos_por_partido"]))
        case "17":
            print(calcular_mostrar_mayor_logro(lista_dream_team))
        case "18":
            print(mayor_al_dato_ingresado_nombres(lista_dream_team,"porcentaje_tiros_triples"))
        case "19":
            calcular_mostrar_mayor_dato(lista_dream_team,"temporadas")
        case "20":
            lista_mayor_porcentaje = mayor_al_dato_ingresado_posicion(lista_dream_team,"porcentaje_tiros_de_campo")##FALTA
            print(listar_jugadores_posicion(lista_mayor_porcentaje))
        case "23":
            ###
            lista_ppp = ordenamiento(lista_dream_team,"puntos_totales")
            lista_rpa = ordenamiento(lista_dream_team,"rebotes_totales")
            lista_apa = ordenamiento(lista_dream_team,"asistencias_totales")
            lista_robos = ordenamiento(lista_dream_team,"robos_totales")
            lista_ppp_ordenada = []
            print("lista puntos")
            for jugador in range(len(lista_ppp)):
                lista_ppp_ordenada.append("{0},{1}".format(lista_ppp[jugador]["nombre"],jugador+1))
            print("lista reb")
            for jugador in lista_rpa:
                print(jugador["nombre"])
            print("lista asis")
            for jugador in lista_apa:
                print(jugador["nombre"])
            print("lista robos")
            for jugador in lista_robos:
                print(jugador["nombre"])            
  
        case "0":
            break
        case _:
            print("Seleccion invalida")

"""
Falta el punto 23
Falta documentar las funciones (escribir que reciben, que hacen y que devuelven)
Falta cambiar el case 24 > por el case 0

"""