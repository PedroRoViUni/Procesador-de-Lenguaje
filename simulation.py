#!/usr/bin/python3
# -- coding: utf-8 --
'''Simulador'''

import networkx as nx
import matplotlib.pyplot as plt
import ply.yacc as yacc
from lexer import tokens

G = nx.Graph()

def simulation(hogar):
    consNodos(hogar.Habitaciones)
    consAristas(hogar.Accesos)
    
    crearSensores(diccionarios())
    for regla in hogar.Reglas:
        if comprobarRegla(regla):
            print(True)
    
    
    print(" _____                        _____  _\n" +     
          "|  __ \                      |  __ \| |\n" + 
          "| |  | | ___  _ __ ___   ___ | |__) | |\n" + 
          "| |  | |/ _ \| '_ ` _ \ / _ \|  ___/| |\n" +     
          "| |__| | (_) | | | | | | (_) | |    | |____ \n" +
          "|_____/ \___/|_| |_| |_|\___/|_|    |______|")
    print("\033[1m"+"| BIENVENID@.\n| Seleccione una opcion:"+"\033[0m")
    print("| 1.-  Comenzar simulacion.\n| X.-   Salir de la aplicacion.")
    opcion = input()
    if opcion == "1":
        drawgraph()

    else: 
        print("¡Hasta pronto!")
        quit()

def consNodos(habitaciones):
    for hab in habitaciones:
        G.add_node(hab.id)
        atributos = {'hab': hab}
        G.add_node(hab.id, **atributos)

def consAristas(accesos):
    for acc in accesos:
        G.add_edge(acc.id1, acc.id2)

def drawgraph():
    plt.ion()

    pos = nx.spring_layout(G)
    for n, p in pos.items():
        G.nodes[n]['pos'] = p  

    nx.draw(G,pos=pos,with_labels=True, edge_color="red",
        node_color="tab:red",node_size=10000,
        font_color="white",font_size=15,font_family="Times New Roman", font_weight="bold",
        width=5)
    
    for node in G.nodes():
        consLabel(node, pos)

    plt.margins(0.2)
    plt.show(block=False)
    menuPrincipal()

def menuPrincipal():
    i = 0
    print("\033[1m"+"\nSelecciona la habitacion en la que comenzar la simulacion:"+"\033[0m")
    habitaciones = list(G.nodes())
    for hab in habitaciones:
        print(str(i) + ".-   Habitacion " + hab)
        i += 1
    while True:
        try:
            opcion = int(input())
            while opcion < 0 or opcion > len(habitaciones)-1:
                print("Opcion fuera de rango, pruebe de nuevo.")
                opcion = int(input())
            break
        except ValueError:
            print('Please enter an integer.')

    node = habitaciones[opcion]
    updateNode(node)
    menu(node)

def updateNode(node):
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[node], node_color="tab:green", node_size=10000)

def menu(node):
    i = 0
    print("\033[1m"+"\nSe encuentra en " + node + ". ¿Que accion desea realizar a continuacion?"+"\033[0m")
    print("1.-  Cambiar valor de sensores.\n2.-  Moverse hacia habitacion accesible.\nX.-  Salir de la aplicacion.")
    opcion = input()

    if opcion=="1":
        updateSensor(node)

    elif opcion=="2":
        print("\033[1m"+"\nIntroduzca la habitacion deseada: "+"\033[0m")
        vecinos = list(G.neighbors(node))
        for vec in vecinos:
            print(str(i) + ".-   Habitacion " + vec)
            i += 1
        while True:
            try:
                opcion = int(input())
                while opcion < 0 or opcion > len(vecinos)-1:
                    print("Opcion fuera de rango, pruebe de nuevo.")
                    opcion = int(input())
                break
            except ValueError:
                print('Please enter an integer.')
        nodeVec = vecinos[opcion]
        print(nodeVec)
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[node], node_color="tab:red", node_size=10000)
        updateNode(nodeVec)
        menu(nodeVec)

    else:
        quit()

def updateSensor(node):
    i = 0
    print("\033[1m"+"\n¿Que sensor quiere modificar?"+"\033[0m")
    sensores = G.nodes[node]['hab'].arraySensores
    for sen in sensores:
        print(str(i) + ".-   Sensor " + sen.id + " " + sen.tipo + " = " + sen.valor)
        i += 1
    while True:
        try:
            opcion = int(input())
            while opcion < 0 or opcion > len(sensores):
                print("Opcion fuera de rango, pruebe de nuevo.")
                opcion = int(input())
            break
        except ValueError:
            print('Por favor, introduzca un entero.')

    print("Ha seleccionado el sensor " + sensores[opcion].id + " de tipo " + sensores[opcion].tipo + ", introduzca su nuevo valor: ")
    entrada = inputTipo(sensores[opcion].tipo)
    sensores[opcion].valor = str(entrada)

    plt.clf()
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G,pos=pos,with_labels=True, edge_color="red",
        node_color="tab:red",node_size=10000,
        font_color="white",font_size=15,font_family="Times New Roman", font_weight="bold",
        width=5)

    for n in G.nodes():
        consLabel(n, pos)

    plt.margins(0.2)
    updateNode(node)
    menu(node)

def consLabel(n, pos):
    sensores = []
    actuadores = []

    pos_labels_sens = {node: (pos[node][0], pos[node][1] - 0.3) for node in G.nodes()}
    pos_labels_acts = {node: (pos[node][0], pos[node][1] + 0.3) for node in G.nodes()}

    for sen in G.nodes[n]['hab'].arraySensores:
        sensores.append(sen.id + " " + sen.tipo + " = " + sen.valor + "\n")
    
    for act in G.nodes[n]['hab'].arrayActuadores:
        actuadores.append(act.id + " " + act.tipo + " = " + act.accion + "\n")

    sens = "".join(sensores)
    acts = "".join(actuadores)
    labels_sens = {}
    labels_acts = {}
    labels_sens[n] = sens
    labels_acts[n] = acts

    nx.draw_networkx_labels(G, pos=pos_labels_sens, labels=labels_sens, font_size=10, font_family="Times New Roman", font_weight="bold")
    nx.draw_networkx_labels(G, pos=pos_labels_acts, labels=labels_acts, font_size=10, font_family="Times New Roman", font_weight="bold")

def inputTipo(tipo):
    if tipo == 'lum':
        entrada = valorNum(0, 100, tipo)
    elif tipo == 'tem':
        entrada = valorNum(0, 50, tipo)
    elif tipo == 'pre':
        entrada = valorNum(0, 100, tipo)
    elif tipo == 'gas':
        entrada = valorBool(tipo)
    elif tipo == 'fue':
        entrada = valorBool(tipo)
    elif tipo == 'hum':
        entrada = valorNum(0, 100, tipo)
    return entrada


def valorNum(numInicial, numFinal, tipo):
    while True:
        try:
            opcion = int(input())
            while opcion < numInicial or opcion > numFinal:
                print("El tipo de sensor " + str(tipo) + ", solo admite enteros entre " + str(numInicial) + " y " + str(numFinal) + ". Pruebe de nuevo:")
                opcion = int(input())
            break
        except ValueError:
            print("Por favor, introduzca un entero.")  
    return opcion

def valorBool(tipo):
    opcion = input()
    while opcion not in ['True', 'False']:
        print("El tipo de sensor " + tipo + ", solo admite los valores True y False. Pruebe de nuevo:")
        opcion = input()
    return opcion

def diccionarios():
    dicSensores = {}
    for node in G.nodes():
        for sensor in G.nodes[node]['hab'].arraySensores:
            id_sensor = sensor.id
            valor = sensor.valor
            dicSensores[id_sensor] = valor
    return dicSensores

def crearSensores(dicSensores):
    
    for sensor in dicSensores:
        if dicSensores[sensor] == 'True':
            globals()[sensor] = True
        elif dicSensores[sensor] == 'False':
            globals()[sensor] = False
        else:
            globals()[sensor] = int(dicSensores[sensor])
        
def comprobarRegla(regla):
    resultado = False
    condicion="" 
    i=0
    while i<len(regla.Condiciones):
        condicion+=regla.Condiciones[i].id + regla.Condiciones[i].simbolo + regla.Condiciones[i].valor   
        i+=1
        if i==len(regla.Condiciones):
            break
        condicion+=" "+regla.Condiciones[i]+" "
        i+=1
    resultado=eval(condicion)
    return resultado