class Animal:
    #Atributos
    #Atributos estaticos
    nombre=""
    edad=0
    #Metodos
    #Metodo Constructor
    def __init__(self,n,e):
        self.nombre=n 
        self.edad=e 
    #Metodos propios de la clase siembre self
    def registrarAnimal(self):
        self.nombre = input("Inregistrar Nombre: ")
        self.edad = int(input("Inregistrar Edad: "))
    
    def mostrarAnimal(self):
        print(f"El Nombre del animal es {self.nombre} y la edad es {self.edad}")
        
    
    
    #Cambiar nombre
    def cambiarNombre(self):
        cambiarNombre=input("Dihite el nuevo nombre")
        self.nombre=cambiarNombre
        print("El nuevo nombre es",self.nombre)
        
    #duplicarEdad pedir edad, retornar esa edad publicada
    def duplicarEdad(self,edad):
        duplicar=edad*2
        return duplicar    

#Crear un odjetio o Instanciar un odjeto
#tigre=Animal()
#tigre.nombre="Tony"
#tigre.edad=5
#print(tigre.nombre,"ooo",tigre.edad)

#panda=Animal()

#panda.nombre="Toto"
#panda.edad=10
#print(panda.nombre,"ooo",panda.edad)

