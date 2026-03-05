class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

A=Persona('Juan')
B=Persona('Andres')
print(A)
print(B)
A=B
A.nombre='Jorge'
print(B.nombre)    
print(A)
print(B)