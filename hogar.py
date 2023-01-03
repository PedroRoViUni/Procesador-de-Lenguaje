
import networkx as nx


class Hogar:
    
    def __init__(self, idHogar, Habitaciones, Accesos, Reglas):
        self.idHogar=idHogar
        self.Habitaciones=Habitaciones
        self.Accesos=Accesos
        self.Reglas=Reglas
        
    def crearGrafo(self, Habitaciones, Accesos):
        grafo = nx.Graph()
        for habitacion in Habitaciones:
            grafo.add_node(habitacion.id)
        for acceso in Accesos:
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
    
        
# class Condiciones:
#     def __init__(self, condicion):
#         self.condicion = condicion
#     def __str__(self) -> str:
#         return self.condicion

class Consecuencia:
    def __init__(self, idActuador, variable):
        self.idActuador=idActuador
        self.variable=variable

class Regla:
    def __init__(self, Condiciones, Consecuencias):
        self.Condiciones=Condiciones
        self.Consecuencias=Consecuencias
    def __str__(self) -> str:
        return self.Condiciones
        
class Dimension:
    
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2

class Sensor:
        
        def __init__(self, id, tipo, valor):
            self.id=id
            self.tipo=tipo
            self.valor=valor
        def __str__(self) -> str:
            return self.id

class Actuador:
        
        def __init__(self, id, tipo, accion):
            self.id=id
            self.tipo=tipo
            self.accion=accion
        def __str__(self) -> str:
            return self.id
