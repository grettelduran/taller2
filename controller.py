from model import Student
from model import Course
from vista import StudentView

from os import system, name  # TO CLEAN THE TERMINAL

class Controller:

    def __init__(self):
        # init construct
        self.course = Course("Curso 1",4)  # creacion de lista para almacenar instancias del modelo estudiante
        self.vista = StudentView() # inicializacion de la Vista
        self.vista.welcome() # mensaje de bienvenida


    def addStudent(self,estudiante): 
        # agregar instancia estudiante a mi lista
        self.course.addStudent(estudiante)


    def updateView(self): 
        # despliego cantidad estudiantes existentes
        self.vista.mensaje("LISTA DE ESTUDIANTES: "+ str(len(self.course.students))) 
        # top message cada vez que se despliega el contenido de lista

        if len(self.course.students)==0: # si la lista esta vacia
            self.vista.mensaje("No se han ingresado datos aun!") # utilizo la vista para enviar mensaje

        else: # si len>0 
            for estudiante in self.course.students: # recorre items per iterable obj
                self.vista.ver_estudiante(estudiante) # despleiga la informacion de cada estudiante
    

    def stopProgram(self): # llama a la vista 
        self.vista.goodbye() # para su mensaje de despedida

    def cleanTerminal(self):
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # mac and linux(os.name = 'posix') 
        else: 
            _ = system('clear') 


    def agregar(self): 
        # metodo del controller para solicitar datos e ingresar nuevo estudiante
        try:
            userInput = str(input("Desea agregar un estudiante? Y/N")) 
            # dentro de un try , asi como cualquier interaccion 
            # con el mundo exterior debe ser anti-errores

            if userInput=='Y':
                datos_newStudent = input("Ingrese el codigo, el nombre, edad y sexo separado por coma-> COD,Nombre Apellido [Sin espacios al inicio]: ").split(',') 
                # con split puedo capturar varios inputs del usuario
                estudiante_nuevo = Student(datos_newStudent[0], datos_newStudent[1], datos_newStudent[2],datos_newStudent[3]) 
                # accedo al indice 0 y 1 para capturar los datos de mi nuevo estudiante
                self.addStudent(estudiante_nuevo)
                # se crea una instancia con los datos capturados
 
        except:
            # para capturar errores
            self.vista.mensaje("Error en la entrada del usuario") 


    def run(self):
        """ como se corre el programa es un loop
        evaluado por el boolean -corriendo- que cambiara a False hasta que el 
        usuario elija no continuar. 
        
        Nota: Entre mas dividida este toda logica en mas y mas metodos, es mejor practica.
        Cada funcion debe hacer SOLO UN OBJETIVO. -> una mision x funcion"""
        corriendo = True
        userInput = None

        while corriendo == True:
            try: # loop que ejecuta el programa
                if userInput==None:
                    userInput = input("Y to display list and continue /N to exit /O for more options: ")
                if userInput == 'Y':
                    self.updateView() # el controller maneja las interacciones entre la vista
                    userInput = input("Y to display list and continue /N to exit /O for more options: ")
                elif userInput=='N':
                    self.stopProgram()
                    corriendo=False
                else:
                    self.agregar() # el modelo, el modelo y la vista no interactuan directamente
                    self.updateView() 
                    self.vista.mensaje("Gracias por utilizar -- Re-starting.../// (...loading...)")
                    userInput = input("Desea volver a utilizarlo? Y to continue /N to exit: ")
                    self.cleanTerminal()
            except:
                self.vista.mensaje("Error en la entrada del usuario")


# notedese que si alguien viera el codigo de run() no puede ver dentro de la clase vista o el modelo como tal
# sino que son metodos de la misma clase controller que encapsulan el acceso a estos.

# metodo main
if __name__=="__main__":
    control= Controller()
    control.run()
                    

