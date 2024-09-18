print (" -- PROGRAMACIÓN POO -- ")

## DEFINICION DE CLASES
class Perro:
#FUNCIONES DENTRO DE LA CLASE
    def morder(self):
        print("El perro me mordió")
    def Datos_perro(self,nombre,edad):
        print(f"Nombre: {nombre}. Edad: {edad}")

## ZONA DE CREACION DE OBJETOS
pitbull=Perro()

## ZONA DE USO DE OBJETOS
pitbull.Datos_perro("Toby", 4)
pitbull.morder()

