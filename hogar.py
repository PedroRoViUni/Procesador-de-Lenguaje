
import networkx as nx
import graphviz


class Hogar:
    
    def __init__(self, idHogar, arrayHabitaciones, arrayAccesos, arrayReglas):
        self.idHogar=idHogar
        self.arrayHabitaciones=arrayHabitaciones
        self.arrayAccesos=arrayAccesos
        self.arrayReglas=arrayReglas
        
    def crearGrafo(self, arrayHabitaciones, arrayAccesos):
        grafo = nx.Graph()
        for habitacion in arrayHabitaciones:
            grafo.add_node(habitacion.id)
        for acceso in arrayAccesos:
            grafo.add_edge(acceso.id1, acceso.id2)
            
    def exportarGrafo(self,grafo,idHogar):
        A = nx.nx_agraph.to_agraph(grafo)
        A.layout('dot')
        A.draw(str(idHogar)+".png")
        # guardar grafo
            #nx.write_graphml(G, "grafo.graphml")
        # cargar grafo
            #G2 = nx.read_graphml("grafo.graphml")  
            
class Acceso:
    
    def __init__(self,id1, id2):
        self.id1=id1
        self.id2=id2
        
class Habitacion:

    def __init__(self, id, ancho, largo, arraySensores, arrayActuadores ):
        self.id=id
        self.ancho=ancho
        self.largo=largo
        self.arraySensores=arraySensores
        self.arrayActuadores=arrayActuadores
    
        
class Norma:

    def __init__(self, simbolo):
        self.simbolo=simbolo

class Normas:
     def __init__(self, id, simbolo, valor):
        self.id=id
        self.simbolo=simbolo
        self.valor=valor
        

class Dimension:
    
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

class Sensor:
        
        def __init__(self, id, tipo, dimension):
            self.id=id
            self.tipo=tipo
            self.dimension=dimension

class Actuador:
        
        def __init__(self, id, tipo, dimension):
            self.id=id
            self.tipo=tipo
            self.dimension=dimension
