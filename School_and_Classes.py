class School:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        
        self.classrooms={}
        self.teacher={}
        
        
        
    def add_classroom(self,classroom):
        self.classrooms[classroom.class_name]=classroom
    
    def add_teacher(self,subject,teacher):
        self.teacher[subject]=teacher
    
    def student_admission(self,student):
        class_name=student.classroom.class_name
        if class_name in self.classrooms:
            self.classrooms[class_name].add_Student(student)
        
        else:
            print(f"Not Found in classroom {class_name}")
            
    @staticmethod
    # def Grade_calculator(marks,student_name=""):
    def Grade_calculator(marks):
        # print(type(marks))
        # print(f"\nGrades for {student_name}:")
        # for key,value in marks.items():
        #     if 100 <= value >=80:
        #         print( f"{key}-----A+")
                
        #     elif 80 <= value >=70:
        #         print( f"{key}-----B+")
                
        #     elif 70 <= value >=60:
        #         print( f"{key}-----B")
                
        #     elif 60 <= value >=50:
        #         print( f"{key}-----C+")
                
        #     elif 50 <= value >=40:
        #         print( f"{key}-----C")
                
        #     elif 40 <= value >=30:
        #         print( f"{key}-----D")
                
        #     else:
        #         print( f"{key}-----F")
        
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
    
    
    def __repr__(self):
        for classrom_key,classrom_value in self.classrooms.items():
            print( f"{classrom_key}--------{classrom_value.class_name}")
        
        print("\n----All Subject Are----\n")
        eight=self.classrooms["Eight"]
        for subject in eight.subjects:
            print(subject.name,subject.teacher.name)
        
        print("\n----All Student Are----\n")  
        for student in eight.students:
            print(student.name,student.getSerial_id)
            
        print("\n----All Student Marks----\n")
        
        for student in eight.students:
            # for key,value in student.marks.items():
            for key , value in student.subject_grade.items():
                print(student.name,key,value)
            print("\nExam Done\n")
        
        return ""

class Classroom:
    def __init__(self,class_name):
        self.class_name=class_name
        
        self.students=[]
        
        self.subjects=[]
    
    def add_Student(self,Student):
        Student.getSerial_id=f"Class {self.class_name} ------ Serial id : {len(self.students)+1}"
        self.students.append(Student)
    
    def add_subject(self,subject):
        self.subjects.append(subject)
    
    
    def take_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        
        for student in self.students:
            student.Calculate_final_Grade()

        