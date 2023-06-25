#Crear odjetos des de otros archivos, ojo importacion
from animal import Animal

panda=Animal()
panda.registrarAnimal()
panda.mostrarAnimal()
print("Duplicar edad",panda.duplicarEdad(panda.edad),"del animal",panda.nombre)







