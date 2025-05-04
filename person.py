from School_and_Classes import School,Classroom
import random

class Person:
    def __init__(self,name):
        self.name=name
    
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
    
    def Evaluate_Exam(self):
        return random.randint(50,100)
    

class Student (Person):
    def __init__(self, name,classroom):
        self.classroom=classroom
        super().__init__(name)

        self.marks={}
        self.__serial_id=None
        self.subject=None
        self.subject_grade = {}
        self.grade=None
    
    @property
    def getSerial_id(self):
        return self.__serial_id
    
    @getSerial_id.setter
    def getSerial_id(self,id):
        self.__serial_id=id

    def Calculate_final_Grade(self):
        sum=0
        for grade in self.subject_grade.values():
            
            point=School.grade_to_point(grade)
            sum+=point
        
            print(self.name,grade,point)
        point_avg=sum/len(self.subject_grade)
        self.grade=School.vlaue_to_Grade(point_avg)
        
        print(f"{self.name} Final Grade {self.grade} WIth Avarage Point {point_avg}\n")