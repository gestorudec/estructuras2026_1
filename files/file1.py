with open('files\\intro4.txt','w') as x:
    x.write('test')




with open('files/intro1.txt','r') as f:    
    #f.write("\n soy creador de oportunidades")
    contenido=f.readlines()

print(contenido)
# for linea in contenido:
#     print(linea)

print(f"contenido ={len(contenido)}")
n=1
for i in range(len(contenido)):
    if n==i:
        print(contenido[i])

    
frase="oh gloria inmarcesible"
lista=frase.split()
print(lista)
    