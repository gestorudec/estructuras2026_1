from Felino import Felino
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class Lista:
    def __init__(self):
        self.primero=None
            
    def adicionar(self,dato):
        nuevo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevo
        else:
           actual=self.primero
           while actual.siguiente:
               actual=actual.siguiente
           actual.siguiente=nuevo
    
    def mostrar(self):
        actual=self.primero
        while actual:
            print(actual.dato)            
            actual=actual.siguiente      

listado=Lista()

g1=Felino("Felino","Leon")
g2=Felino("Felino","Tigre")
g3=Felino("Felino","Lince")
g4=Felino("Felino","Puma")

listado.adicionar(g1)
listado.adicionar(g2)
listado.adicionar(g3)
listado.adicionar(g4)
listado.mostrar()

    
    