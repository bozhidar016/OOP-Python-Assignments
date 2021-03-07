import abc
class Studenti(abc.ABC):
    def __init__(self, name, adress, phone, course, index_number):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.course = course
        self.index_number = index_number
    @abc.abstractclassmethod
    def getInfo(self):
        pass
        
class Student(Studenti):
    def getInfo(self):
        print("Name :", self.name, ",", "Adress :", self.adress, ",", "Phone :", self.phone, ",", "Course :", self.course, ",", "Index number :", self.index_number)
student1 = Student("Nikola Nikolic", "Stepe Stepanovic 193", "065/889-332","Python programming", "310/20")
student1.getInfo()
student2 = Student("Marko Markovic", "Bulevar oslobodjenja 20", "063/332-23-33", "Python programming", "250/20")
student2.getInfo()
student3 = Student("Petar Petrovic", "Jovana Cvijica", "064/239-03-23", "Python programming", "192/19")
student3.getInfo()