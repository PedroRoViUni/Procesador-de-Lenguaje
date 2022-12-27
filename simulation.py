#!/usr/bin/python3
# -- coding: utf-8 --
'''Simulador'''

import networkx as nx
import graphviz as gp
import matplotlib.pyplot as plt

G = nx.Graph()

def drawgraph(hogar):
    habitaciones = hogar.Habitaciones
    accesos = hogar.Accesos
    reglas = hogar.Reglas
    consHabitaciones(habitaciones)
    consAccesos(accesos)

    pos = nx.spring_layout(G)
    labels_sens = {node: f"\n".join(G.nodes[node]['sensores']) for node in G.nodes()}
    labels_acts = {node: f"\n".join(G.nodes[node]['actuadores']) for node in G.nodes()} 
       
    nx.draw(G,pos=pos,with_labels=True, edge_color="red",
        node_color="red",node_size=10000,
        font_color="white",font_size=15,font_family="Times New Roman", font_weight="bold",
        width=5)

    pos_labels_sens = {node: (pos[node][0], pos[node][1] - 0.3) for node in G.nodes()}
    pos_labels_acts = {node: (pos[node][0], pos[node][1] + 0.3) for node in G.nodes()}

    nx.draw_networkx_labels(G, pos=pos_labels_sens, labels=labels_sens, font_size=10, font_family="Times New Roman", font_weight="bold")
    nx.draw_networkx_labels(G, pos=pos_labels_acts, labels=labels_acts, font_size=10, font_family="Times New Roman", font_weight="bold")

    plt.margins(0.2)
    plt.show()

def consHabitaciones(habitaciones):
    for hab in habitaciones:
        sensores = hab.arraySensores
        actuadores = hab.arrayActuadores
        sens = []
        acts = []
        for sen in sensores:
            sens.append(sen.id + " " + sen.tipo + " = " + sen.valor)

        for act in actuadores:
            acts.append(act.id + " " + act.tipo + " = " + act.accion)

        atributos = {'sensores': sens, 'actuadores': acts}
        G.add_node(hab.id, **atributos)

def consAccesos(accesos):
    for acc in accesos:
        G.add_edge(acc.id1, acc.id2)

