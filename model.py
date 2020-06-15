""""Estructura de una aplicación MVC
Definición de Modelos
Modelo: Incluye todos los datos y su lógica relacionada.

Definicion de Vistas
Vista: presentar datos al usuario o manejar la interacción del usuario (entrega las entradas del usuario)

Definición de controladores
Controlador: una interfaz entre los componentes Modelo y Vista"""

class Course():
    """bluePrint of a course"""
    
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.students = []
    def addStudent(self, student):
        self.students.append(student)
class Student():
    """bluePrint of a student"""

    def __init__(self,studentId,name,age,gender):
        self.studentId=studentId
        self.name=name
        self.age=age
        self.gender=gender
        print("Cod: {} \nNombre: {}\nEdad: {}\nGenero: {}".format(self.studentId,self.name,self.age,self.gender))

