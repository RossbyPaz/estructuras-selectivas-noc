#Estructura simple
a= 33
b = 200

if b > a:
    print(b, "es mayor que",a)

#Condcion estructura doble

if a > b:
    print(a,"es mayor que ",b)
else:
    print(a,"no es mayor que",b)

#Condicion multiple
c = 200
d = 207
if a > b:
    print(c,"es mayor que",d)
elif a < b:
    print(c, "es menor que",d)
else:
    print(c,"es igual que",d)
#Condiciones Enlazadas
x = 28

if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y también por encima de 20!")
    else:
        print("pero no por encima de 20")
#Paarámetros end y sep
#Parametro end= evita que el print de un salto de linea. podemos agregar dentro de las comillas lo que queramos

print("Estudiar los sabados,")
print("es genial")

print("Estudiar los sabados", end=" ")
print("es genial")

#Parametro sep
#coloca debajo de los nombre un _
print("Daniela","Luis","Carlos","camila",)#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","camila", sep="")#quita el espacio
print("Daniela","Luis","Carlos","camila", sep=",")#Agrega una coma

print("Daniela","Luis","Carlos","camila", sep="_", end="_Curso_Python")#implementación end y sep

