# Vamos a partir definiendo mi agrupación (clase)
# En este caso, definiremos la agrupación o clase Persona

class Persona:
    # Dentro de la definición de la clase (indicada con
    # los espacios de tabulación, crearemos las características
    # de nuestra clase (ATRIBUTOS) y sus acciones o funcionalides
    # (MÉTODOS), donde estos atributos y métodos pueden ser
    # utilizados por cualquier objeto que pertenezca a esta clase
    # (Persona).
    
    # Todo objeto creado a partir de la clase Persona DEBE tener valores iniciales
    # para los atributos que definamos en ella. Para ello, existe una funcionalidad
    # especial (un método de clase especial) que solo se encarga de inicializar estos
    # atributos para un objeto puntual. Este método se llama "método constructor".
    def __init__(self, edad, peso, estatura, nombre):
        # El método __init__() corresponde al método constructor de la clase.
        # Es decir, aquel método encargado de crear (construir) el objeto
        # con el estado inicial que este tenga.
        
        # Por lo tanto utilizaremos este método para crear e inicializar los atributos
        # de la clase.
        
        # El parámetro self del constructor (y de cualquier método de clase) se utiliza
        # para indicar de manera explícita a dicho método cuál es el objeto que llamó a
        # ese método.
        
        # A continuación creamos los atributos de la clase, los cuales son inicializados
        # con los parámetros de entrada de nuestro constructor
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.nombre = nombre
        
    # En el constructor hemos creado los atributos de la clase y los hemos inicializado.
    # Lo que nos falta ahora es crear los métodos de esta clase, para que puedan realizar
    # acciones
    
    def correr(self):
        print("Estoy corriendo! :D")
        
    def getPeso(self):
        return self.peso
    
    def cumple(self):
        self.edad = self.edad + 1
        
    def cambioNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
# En este punto, ya tenemos definida una clase con sus métodos y atributos internos.
# Pero, recordemos que la clase define simplemente características y acciones que puede
# realizar un cierto conjunto de elementos.
# La pregunta que viene a continuación es cómo podemos crear elementos que pertenezcan a esta
# agrupación que hemos definido? O, en otras palabras, cómo podemos crear objetos que 
# pertenezcan a la clase Persona en este ejemplo?

# Cuando hemos creado variables con anterioridad, ya hemos estado trabajando con objetos.
# Al crear una variable y asignarle un valor, ese valor se "encapsula" en un objeto y 
# es ese objeto el que se asigna a la variable que hemos creado.
a = 10 
print(type(a))

# Reutilzando estos mismos conceptos, podemos crear objetos a partir de la clase que hemos definido
personaA = Persona(27, 73, 1.82,"Camilo") # La notación NombreClase(...) Python lo entiende como que estamos llamando
# al método constructor de la clase NombreClase
# Luego de esta línea, tenemos almacenada en la variable "personaA" un objeto de la clase Persona
# A partir de personaA, podemos acceder a todas los atributos y métodos definidos para cualquier Persona
# Accediendo a algunos atributos
print("Hola, me llamo", personaA.nombre, ", tengo", personaA.edad, "años y mido", personaA.estatura, "mts")
# Accediendo a algunos métodos
personaA.correr()

# Por supuesto, la gracia de crear clases y objetos es que puedes tener múltiples objetos que pertenecen
# a una misma clase!!
personaB = Persona(35, 86, 1.78, "Francisca")
personaB.correr()

class Curso:
    def __init__(self, nombre_curso, duracion):
        self.nombre_curso = nombre_curso
        self.duracion = duracion

# Herencia es el concepto que aplica la programación orientada a objetos y que permite reutilizar
# lo desarrollado (definido) en una clase como la base para la creación de otras clases.
# Ejemplo. Podemos crear la clase Estudiante utilizando la clase Persona como base. Esto 
# tiene sentido porque "TODO ESTUDIANTE ES AL MISMO TIEMPO PERSONA". Esto, en programación 
# orientada a objetos se dice como "La clase Estudiante HEREDA de la clase Persona"
class Estudiante(Persona): # Esta es la notación que indica la herencia de Estudiante desde Persona
    def __init__(self, edad, peso, estatura, nombre, curso):
        # Para inicializar nuestro estudiante, primero debemos inicializar todos aquellos atributos
        # que provienen de Persona. Para ello, debo llamar al constructor que definimos en la clase
        # Persona. Con super() estamos llamando a la súper clase (Persona).
        super().__init__(edad, peso, estatura, nombre) # Esta línea inicializa todo lo de Persona
        # A continuación inicializamos los atributos específicos del estudiante
        self.curso = curso 
        # En este punto tenemos un estudiante con todos sus atributos, tanto los de Persona
        # como los propios del estudiante, inicializados.
        
nuevo_curso = Curso("Python", 8)
nuevo_estudiante = Estudiante(20, 66, 1.59, "Alonso", nuevo_curso)

