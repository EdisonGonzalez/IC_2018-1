
# coding: utf-8

# In[1]:


#Este es un comentario porque empieza con #

#Esta es una celda de código. 

#Se ejecuta con ctrl+enter. Probalo.

#La función print puede imprimir varias cosas
print("Hola Mundo") #impresión de un string
print(4) # impresión de un número

#Intentá imprimir el string "IMAGENES":


# In[2]:


x="hola"
print(x)

x=5
print(x)

y=x+2.5
print(y)


# In[3]:


### Enteros ###

x = 3 

print("- Tipo de x:")
print(type(x)) # Imprime el tipo (o `clase`) de x
print("- Valor de x:")
print(x)       # Imprimir un valor
print("- x+1:")
print(x + 1)   # Suma: imprime "4"
print("- x-1:")
print(x - 1)   # Resta; imprime "2"
print("- x*2:")
print(x * 2)   # Multiplicación; imprime "6"
print("- x^2:")
print(x ** 2)  # Exponenciación; imprime "9"
# Modificación de x
x += 1 
print("- x modificado:")
print(x)  # Imprime "4"

x *= 2
print("- x modificado:")
print(x)  # Imprime "8"

print("- Varias cosas en una línea:")
print(1,2,x,5*2) # imprime varias cosas a la vez


# In[4]:


### Flotantes ###

y = 2.5 
print("- Tipo de y:")
print(type(y)) # Imprime el tipo de y
print("- Varios valores en punto flotante:")
print(y, y + 1, y * 2.5, y ** 2) # Imprime varios números en punto flotante


# In[5]:


### Booleanos ###

v1 = True #el valor verdadero se escribe True 
v2 = False #el valor verdadero se escribe False

print("- Valores de v1 y v2:")
print(v1,v2)

print("- Tipo de v1:")
print(type(v1)) # Imprime la clase de un valor booleano ('bool')

print("- v1 and v2:")
print(v1 and v2) # y lógico; imprime False
print(v1 or v2)  # o lógico; imprime True
print(not v1)   # negación lógica, imprime False

print(3 == 5)  # Imprime False ya que son distintos
print(3 != 5)  # Imprime True ya que son distintos
print(3 < 5)  # Imprime True ya que 3 es menor que 5


# In[6]:


print("- Lista con 4 números:")
a=[57,45,7,13] # una lista con cuatro números
print(a)

print("- Lista con 3 strings:")
b=["hola","chau","buen día"] # una lista con tres strings
print(b)

# la función `len` me da la longitud de la lista
print("- Longitud de la lista:")
n=len(a)
print(n)


# In[7]:


#Para acceder a sus elementos, se utiliza el []
# Los índices comienzan en 0
print("- Elemento con índice 0 de la lista:")
print(b[0])
print("- Elemento con índice 1 de la lista:")
print(b[1])
print("- Elemento con índice 2 de la lista:")
print(b[2])


# In[8]:


# para crear una lista vacía, (sin elementos), simplemente ponemos []
vacia=[]
print("Lista vacía:")
print(vacia)

# También podés crear una sub-lista o slice especificando un rango de indices
print("- Elementos del índice 0 al 1 (2-1):")
print(a[0:2])
print("- Elementos del índice 1 al 3 (4-1):")
print(a[1:4])
#Si ponés nada antes del : se asume que pusiste 0
print("- Elementos desde el comienzo al indice 1 (2-1) :")
print(a[:2])
#Si no ponés nada después del : se asume que tomás todos hasta el final
print("- Elementos desde el indice 1 hasta el final:")
print(a[1:])

#Si no pones nada ni antes ni después es como tomar todo
print("- Todos los elementos:")
print(a[:])


#Si el fin es igual al comienzo, es un rango vacío, por ende se obtiene una lista vacía
print("- Rango vacío -> lista vacía:")
print(a[2:2])


# In[9]:


#por último, le podés agregar elementos a una lista con el método `append`
print("- Una lista con 3 strings:")
a=['una','lista','de']
print(a)

print("- La misma lista luego de agregarle un string más:")
a.append('strings')
print(a)


# In[10]:


#Podés crear una tupla con valores entre () separados por ,
a=(1,2,57,4)
print("- Una tupla de cuatro elementos:")
print(a)
print("- El elemento con índice 2:")
print(a[2])
print("- Los elementos entre los índices 0 y 2:")
print(a[0:2])

# la siguiente línea genera un error de ejecución
#a.append(28)


# In[11]:


#Estructuras de control¶
#En Python no hay llaves ({}) ni begin...end para marcar el comienzo y fin de un bloque, sino que eso se logra con la indentación. La indentación por defecto son 4 espacios en blanco.

#Entonces va a ser necesario indentar correctamente para utilizar sentencias if, for o para definir funciones.

#if
#El if es como el de otros lenguajes, pero no pide paréntesis y termina con :. Su sintaxis es:

#if condicion :
#    cuerpo del if (indentado con 4 espacios)
#else:
#    cuerpo del else (indentado con 4 espacios)

edad = 25

print("La persona es")
if edad < 18: # el if termina con : para indicar donde acaba la condición
    # el print va indentado con 4 espacios para indicar que está dentro del
    # cuerpo del if
    print("Menor") 
else:
    #Lo mismo con este print
    print("Mayor")
    
print("De edad")


# In[12]:


#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel`

pixel= [0.6,0.3,0.4] # intensidades de cada canal. 
#El elemento 0 es el R, el 1 el G y el 2 el B

# la intensidad en escala de grises es el promedio de la intensidad de cada canal R, G y B
intensidad=0 # IMPLEMENTAR

print("La intensidad es:")
print(intensidad)


# In[13]:


#Ejercicio
# Pasar a blanco y negro el valor de intensidad codificado en la variable intensidad


# podemos considerar que un pixel se convierte en blanco si su intensidad en escala de grises es mayor a 0.5
# y negro de lo contrario
bw = 0 # IMPLEMENTAR

print("En blanco y negro el pixel sería: (0 -> negro, 1 -> blanco)")
print(bw)


# In[14]:


#For
#Los for son parecidos a los if, pero tienen la sintaxis for variable in lista:. En este caso, variable es la variable que va a ir cambiando, y lista es una lista de python (o un iterable que es parecido)

print("- Impresion de los elementos de la lista:")

# Imprimir los strings de mi_lista por separado
mi_lista=["img","python","numpy"]
for s in mi_lista:
    print(s)# este print va con indentación
    
#calcular la suma de los números e imprimirla
suma=0
mis_numeros=[5,8,17,12]
for numero in mis_numeros:
    suma=suma+numero
print("- La suma de los números es:")
print(suma)


# In[15]:


#Cuando no tenemos una lista y queremos hacer un for "común" y que la variable que cambia sea un número que va incrementándose, podemos utilizar la función range.

#un for de 0 a 3, para imprimir esos valores
print("Un for de 0 a 3")
for i in range(4):
    print(i)
    
#En Python los índices comienzan en 0, y por eso los rangos también.
    
#También se puede comenzar el rango en otro valor en lugar de 0
print("- Un for de 2 a 5:")
for j in range(2,6):
    print(j)


# In[16]:


#Ejercicio: Escribir un for para buscar el máximo de la lista e imprimirlo
lista=[44,11,15,29,53,12,30]
maximo=0
# IMPLEMENTAR

# debe imprimir 53
print("- El maximo es:")
print(maximo)


# In[17]:


#Ejercicio: Escribir un for para buscar el máximo de la lista e imprimir su _posición_
lista=[44,11,15,29,53,12,30]
posicion=0
# IMPLEMENTAR

#debe imprimir 4
print("- La posición del máximo es:")
print(posicion)


# In[18]:


#Funciones
#Las funciones se definen con la palabra clave def y tienen la sintaxis def nombre_funcion(parametros):. Para devolver un valor utilizamos la palabra clave  return.

#esta funcion recibe dos números y devuelve su suma

def sumar(a,b):
    return a+b


c=sumar(2,5)
print("2+5=")
print(c)


#esta funcion recibe una lista y devuelve la suma de sus elementos
def sumar_todos(lista):
    suma=0
    for v in lista:
        suma+=v
    return suma

mi_lista=[54,12,99,15]
print("los elementos de la lista suman:")
print(sumar_todos(mi_lista))


# In[19]:


#Ejercicio
# Escribir una función que reciba una lista y un valor, 
#y devuelva la cantidad de veces que aparece ese valor en la lista

def ocurrencias(lista,valor):
    # IMPLEMENTAR
    return 0


l=[1,4,2,3,5,1,4,2,3,6,1,7,1,3,5,1,1,5,3,2]
v=2

print(ocurrencias(l,v))

