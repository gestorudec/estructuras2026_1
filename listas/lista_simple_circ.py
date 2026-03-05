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
            nuevo.siguiente=self.primero            
        else:
           actual=self.primero
           while actual.siguiente !=self.primero:
               actual=actual.siguiente
           actual.siguiente=nuevo
           nuevo.siguiente=self.primero
    
    def mostrar(self,repeticiones=10):
        actual=self.primero
        cont=0
        while actual and cont<repeticiones:
            print(actual.dato,end='-')
            actual=actual.siguiente      
            cont+=1

listado=Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.adicionar(100)
listado.adicionar(202)
listado.mostrar()


# class Persona:
#     def __init__(self,nombre):
#         self.nombre=nombre

# A=Persona('Juan')
# B=Persona('Andres')
# print(A)
# print(B)
# A=B
# A.nombre='Jorge'
# print(B.nombre)    
# print(A)
# print(B)