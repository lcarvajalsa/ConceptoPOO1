class Persona:
    #Atributos
    #Atributos estaticos
    tipoDoc=""
    documento=0
    nombre=""
    apellido=""
    peso=0
    estatura=0.0
    edad=0
    sexo=""
    
    #Metodos
    #Metodo Constructor
    """def __init__(self,t,d,n,a,p,e,ed,s):
        self.tipoDoc=t 
        self.documento=d 
        self.nombre=n 
        self.apellido=a 
        self.peso=p 
        self.estatura=e 
        self.edad=ed 
        self.sexo=s 
     """  
    #Metodos propios de la clase siembre self
    #pedir datos
    def pedirDatos(self):
        self.tipoDoc = input("Ingresar tipo de dato:\n ")
        self.documento = int(input("Ingresar documento:\n "))
        self.nombre = input("Ingresar nombre:\n ")
        self.apellido = input("Ingresar apellido:\n ")
        self.peso = int(input("Ingresar peso: \n"))
        self.estatura = float(input("Ingresar estatura: \n"))
        self.edad = int(input("Ingresar edad:\n "))
        self.sexo = input("Ingresar sexo:\n ")
        
    def mostrarPersona(self):
        print(f"Tipo de Documento {self.tipoDoc}\n {self.documento}\n {self.nombre}\n{self.apellido}\n {self.peso}\n {self.estatura}\n {self.sexo}\n{self.edad}")
        
    def calcularImc(self):
        pesoActual = self.peso/self.estatura**2
        if pesoActual<20:
            print(f"el peso esta por debajo de lo ideal")
        elif pesoActual>=20 and pesoActual<=25:
            print(f"el peso es ideal")
        else:
            print(f"Tiene sobre peso")
            
    def mayorEdad(self):
        if self.edad<18:
            print(f"Eres menor de edad")
        else:
            print("Eres Mayor")
            
        
     
  