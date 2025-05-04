import random
class School:
    def __init__(self,name,address):
        self.name= name
        self.address=address

        self.teachers={}
        self.classrooms={}
        
    
    def Add_teacher(self,teacher,subject):
        self.teachers[subject]=teacher
    
    def Add_classrooms(self,classroom_name):
        if classroom_name not in self.classrooms:
            self.classrooms[classroom_name]=classroom_name
        
    def Student_admission(self,Student):
        class_name=Student.class_name
        if class_name in self.classrooms:
            self.classrooms[class_name].add_student(Student)
            
    @staticmethod

    def Grade_calculator(marks):

        if 100 <= marks >=80:
            return 'A+'
                
        elif 80 < marks >=70:
            return "B+"
        elif 70 < marks >=60:
            return "B"    
        elif 60 < marks >=50:
            return "C+"
        elif 50 < marks >=40:
            return "C"        
        elif 40 < marks >=30:
            return "D"        
        else: 
            return "F" 

    @staticmethod   
    def grade_to_point(grade):
        gradeToPOint={
            'A+': 5.00,
            'B+': 4.00,
            'B' : 3.00,
            'C+': 2.00,
            'C' : 1.00,
            'F' : 0.00,
        }
        return gradeToPOint[grade]
    
    def vlaue_to_Grade(value):
        if 4.5 <= value >=5.0:
            return 'A+'
        elif 3.5 <= value >=4.5:
            return 'A'
        elif 3.0   <= value >=3.5:
            return 'A-'
        elif 2.5 <= value >=3.0:
            return 'B'
        elif 2.5 <= value >=2.0:
            return 'C'
        elif 2.0 <= value >=1.0:
            return 'D'
        else:
            return 'F'
        
        
class Classroom:
    def __init__(self,class_name):
        self.class_name=class_name
        
        self.students=[]
        
        self.Subjects=[]
    
    def add_student(self,student):
        self.students.append(student)
        student.get_serial_id=f" class : {self.class_name} ID: {len(self.students)+1}"
    
    def add_subject(self,Subject):
        self.Subjects.append(Subject)
    
    def Take_exam(self):
        for subject in self.Subjects:
            subject.exam(self.students)

class Subject:
    def __init__(self,subject_name,teacher):
        self.subject_name=subject_name
        self.teacher=teacher
    
    
    def exam(self,students):
        for student in students:
            mark=self.teacher.Evalute_exam()
            student.marks[self.subject_name]=mark
            student.grade[self.subject_name]=School.Grade_calculator(mark)
            
        # student.subject_grade[self.subject_name]=School.grade_to_point(mark)
        

    
class Person:
    def __init__(self,name,contact_no):
        self.name=name
        self.contact_no=contact_no

class Student(Person):
    def __init__(self, name, contact_no,class_name):
        super().__init__(name, contact_no)
        
        self.marks={}
        self.grade={}
        self.class_name=class_name
        self.__id=None
        self.subject_grade={}
        self.student_grade=None
        
        
    @property
    def get_serial_id(self):
        return self.__id
    
    @get_serial_id.setter
    def get_serial_id(self,id):
        self.__id=id

    def Calculate_final_grade(self):
        print("marks item printed\n")
        sum=0
        for key,value in self.grade.items():

            point=self.subject_grade[key]=School.grade_to_point(value)
            sum+=point
            point_avg=sum/len(self.subject_grade)
            
            student_grade=School.vlaue_to_Grade(point_avg)

            print(student.name,key,value,student_grade)
        
    
class Teacher(Person):
    def __init__(self, name, contact_no):
        super().__init__(name, contact_no)
    
    def Evalute_exam(self):
        return random.randint(50,100)
        
HSchool=School("High School","Baradi Bazar")
#make a classroom
Eight=Classroom("Eight")
Nine=Classroom("Nine")
Ten=Classroom("Ten")

#adding classroom to school
HSchool.Add_classrooms(Eight)
HSchool.Add_classrooms(Nine)
HSchool.Add_classrooms(Ten)
# Making & Adding Teacher to The classrooms
Kabir=Teacher("Kabir","01")
Hk=Teacher("Hossain kobir","01")
Siddique=Teacher("Hossain kobir Siddique","01")

#adding subject & teacher
physic=Subject("Physics",Kabir)
HSchool.Add_teacher(Kabir,physic)

chemistry=Subject("Chemisry",Hk)
HSchool.Add_teacher(Hk,chemistry)


biology=Subject("biology",Siddique)
HSchool.Add_teacher(Siddique,biology,)

Eight.add_subject(physic)
Eight.add_subject(chemistry)
Eight.add_subject(biology)

Mahadi=Student("Mahadi","0104..",Eight)
Khan=Student("Khan","0104..",Eight)
shaheb=Student("shaheb","0104..",Eight)

HSchool.Student_admission(Mahadi)
HSchool.Student_admission(Khan)
HSchool.Student_admission(shaheb)

Eight.Take_exam()
Mahadi.Calculate_final_grade()

# print(HSchool)