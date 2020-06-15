
class StudentView:

    def __init__(self):
        self.breakliner = "***********************************"

    def welcome(self):
        print(self.breakliner+'\n'+"Welcome to the M V C Pattern example. ")
        print(self.breakliner+'\n'+ " INSERT YOUR ANSWERS WITH CAPS ")

    def goodbye(self):
        print('\n'+self.breakliner+"Thank you for using the M V C Pattern ")

    def ver_estudiante(self, estudiante):
        print(self.breakliner+'\n'+ estudiante.idEstudiante + " "+estudiante.name)

    def mensaje(self,mensj):
        print(mensj+'\n')
