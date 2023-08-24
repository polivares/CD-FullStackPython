# Este símbolo es el que se utiliza para comentarios de una línea
# Sería equivalente al símbolo // de javascript
''' DOCSTRING
Esto simplemente representa
un comentario de múltiples
líneas.
Este formato se utiliza mucho para la generación de 
documentación.
'''
# Variables
x = 2 # En este caso, creamos una variable x con valor 2
y = 5
z = x + y
# Imprimiremos por pantalla los valores de
# de las variables x, y, z.
# La función print muestra el contenido de lo que se entrega
# por la terminal/consola/pantalla
print(x, y, z)

# ¿Qué cosas puedo almacenar en una variable en Python?
a1 = 10 # Números enteros. Tipo de dato integer - int
a2 = 15.3 # Números con decimales (reales). Tipo de dato flotante - float
# También se pueden almacenar textos. Tipo de dato string - str
a3 = "Este es un texto creado con comillas dobles"
a4 = 'Este es un texto creado con comillas simples'
# También se pueden almacenar valores de verdad lógicos Estos pueden ser
# verdadero (True) y falso (False). Tipo de dato booleano/boolean - bool
a5 = True
# También se pueden guardar números complejos, los cuales están compuestos
# por una parte real y una parte imaginaria.
# La parte real es simplemente un número entero/flotante mientras que la
# parte imaginaria se anota como un número entero/flotante acompañado de
# la letra j.
a6 = 3.3 + 5.1j # Este es un núemero complejo. Parte real 3.3 y parte imaginaria 5.1

print(a1, a2, a3, a4, a5, a6)

# En Python existen los tipos de datos compuestos.
# Existen 4 tipos de datos compuestos: listas, tuplas, rangos (range) y diccionarios
# También existen los objetos (de manera similar a javascript), pero eso es para después :)

# Listas
# lista1 es una variable de tipo lista - list que contiene 3 elementos ordenados
lista1 = [4, 8, 2]
# lista2 es una lista de 5 elementos (se considera la lista interna como un solo elemento)
lista2 = [1, 3.4, 5.1 - 7.8j, "texto", [1, 4.5, "prueba"]]
# No solamente se pueden crear listas con elementos ordenados, sino que, una vez
# creada la lista, se puede acceder a cada uno de los elementos que se encuentren
# en ella.
# Para acceder a cada elemento, se utiliza la notación de índice
# OJO: El índice en las listas parte en CERO. Ej: El primer elemento de una lista
# Python es el elemento con índice 0
print(lista2[4][1])
# Funcionalidades integradas en las listas.
# Cómo podemos agregar un elemento?
# Se puede agregar un elemento a una lista de dos formas diferentes.
# 1) Utilizando el método append(), el cual agrega elementos al final de una lista
lista1.append(20) # Agregamos al final de lista1 el elemento 20
print(lista1)
# 2) Utilizando el método insert(), el cual agrega elementos en CUALQUIER posición de la lista
# Con insert, debes agregar 2 parámetros de entrada: uno indicando lo que quieres agregar, y otro
# indicando el dónde lo agregarás.
lista1.insert(1, "pez")
print(lista1)
# Por solicitud de Yojan, agregaremos un elemento en la lista interna de lista2 (con insert):)
lista2[4].insert(1, "Yojan fue agregado!")
print(lista2)
# Y ahora, cómo podemos eliminar/quitar elementos en una lista?
# Para quitar elementos, utilizaremos el método pop()
elemento = lista1.pop() # Cuando pop() no tiene parámetros de entrada, borra el último elemento (por omisión)
# El método pop(), no solo quita elementos de una lista, sino que también permite utilizar esos elementos 
# sacados de la lista
print(lista1, elemento)
# Si entregamos a pop() una posición, también nos permite quitar elementos de la lista en esa posición.
lista1.pop(1) # En este caso, estamos borrando con pop() el elemento en la posición índice 1 ("pez").
print(lista1)
# Puedo acceder a más de un elemento a la vez en mis listas? R: Sí, se puede! (yuju!)
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Para acceder a un único elemento, utilizábamos la notación de índices, mientras que, para acceder
# a múltiples elementos, utilizaremos una nueva notación: la notación de rangos
# Notación: lista[indice_1er_elemento:indice_elemento_final:salto]
print(lista3[3:7:1])
# Cada uno de los elementos utilizados para indicar el rango, tiene valores por omisión (default)
# indice_1er_elemento: su valor por omisión es el inicio de la lista (índice 0)
# indice_elemento_final: su valor por omisión es el final de la lista (índice -1)
# salto: su valor por omisión es 1
# Ejs
print(lista3[:5:]) # Esto es equivalente a lista3[0:5:1]
print(lista3[::]) # Esto es equivalente a lista3 completa
# La notación de índices y rangos es tan flexible que incluso permite recorrer listas al revés!! :O!!
# Accediendo al último elemento
print(lista3[-1]) # El índice -1 indica que estamos partiendo desde el final de la lista
# Accediendo a rangos de elementos al revés
print(lista3[-1::-1])
# Cómo podemos saber cuál es el largo de una lista?
# Paral calcular el largo de una lista, se puede utilizar la función len(), la cual es una función
# EXTERNA a las listas, pero que se puede utilizar sobre ellas
print(len(lista3)) # len() entrega el largo de la lista3, que en este ejemplo es 11 elementos.
# A petición de Florencia, cómo retroceder hasta la mitad de una lista??
print(lista3[-1:(len(lista3)//2)-1:-1])

# Tuplas: Son básicamente iguales a las listas ....pero SON INMUTABLES.
# Creamos tuplas. La notación es muy similar a la de listas
tupla1 = (1, 2, 3, 4) # Mi primera tupla :D
print(tupla1)
print(tupla1[2]) # Acceso por índices funciona igual que en las listas
# tupla1[2] = 20 # Si descomentas esta línea, lanzará error! no puedes asignar nuevos elementos en una tupla
tupla2 = (1, "hola", [1, 2, 3])
print(tupla2)
# Ojo: en tupla2, sí puedes modificar los elementos DENTRO de la lista interna
# Lo que no puedes hacer es REEMPLAZAR esa lista
tupla2[2][0] = "Primer elemento"  # Esto es válido
print(tupla2)
# tupla2[2] = 4 # Esto NO es válido
# print(tupla2)

# Rangos/range: El rango/range permite crear un conjunto de elementos númericos (de tipo entero) con
# rápidez (además de una ventaja de optimización de memoria).
# Para crear un rango de números, se utiliza la función range() con una notación "similar" a la de rangos
# índices en una lista/tupla
rango1 = range(-5, 5, 1) # Esto genera los números enteros partiendo del -5 hasta el 5 (sin incluir/muralla)
# de 1 en 1
print(rango1)
# El acceso a cada número o subconjunto se realiza con la misma notación de índices y rangos de listas
# y tuplas. Ej.
print(rango1[0]) # Accedo al primer número generado en el rango1
print(rango1[2::2]) # Desde el elemento índice 2 hasta el último de 2 en 2
# Los rangos se puden transformar fácilmente a listas o tuplas utilizando las funciones
# list() y tuple() respectivamente
print("Rango como lista:", list(rango1))
print("Rango como tupla:", tuple(rango1))

# Diccionarios: El diccionario es un tipo de dato compuesto que permite el acceso a sus elementos
# utilizando índices que no son necesariamente numéricos. El índice (llave) puede ser CUALQUIER COSA...
# siempre y cuando esa llave sea un dato INMUTABLE (incluyendo las tuplas!)
dict1 = {
    "llave1": "Elemento asociado a la llave1",
    0: 15,
    (1,2,3): ["Llave tupla para acceder a este elemento", 15.6]
}
print(dict1["llave1"], dict1[0], dict1[(1,2,3)])

# Se puede utilizar la función items() de los diccionarios para mostrar tanto llaves como elemntos
# asociados a un diccionario
print(dict1.items())