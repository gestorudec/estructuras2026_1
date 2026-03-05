class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
class Lista:
    def __init__(self):
        self.cabeza=None
        self.cola=None
    
    def adicionar(self,dato):
        nuevo=Nodo(dato)
        if self.cabeza==None:
            self.cabeza=nuevo
            self.cola=nuevo
            self.cola.siguiente=self.cabeza
            self.cabeza.anterior=self.cola
        else:
            self.cola.siguiente=nuevo
            nuevo.anterior=self.cola
            self.cola=nuevo
            self.cola.siguiente=self.cabeza
            self.cabeza.anterior=self.cola
    def mostrarAdelante(self,repeticiones=10):
        actual=self.cabeza
        cont=0
        while actual and cont<repeticiones:
            print(actual.dato,end='-')
            actual=actual.siguiente
            cont+=1
    def mostrarAtras(self,repeticiones=10):
        actual=self.cola
        cont=0
        while actual and cont<repeticiones:
            print(actual.dato,end='-')
            actual=actual.anterior
            cont+=1
            
listado=Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.adicionar(18)
listado.adicionar(27)
listado.mostrarAdelante()
print("-"*50)
listado.mostrarAtras()