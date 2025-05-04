
from School_and_Classes import School
class Subject:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher
    
    def exam(self,students):
            for student in students:
                mark= self.teacher.Evaluate_Exam()
            
                student.marks[self.name]=mark   
            # for student in students:
            # #     student.marks[self.name].School.Grade_calculator(student.marks)
            #     School.Grade_calculator(student.marks,student.name)
                student.subject_grade[self.name]=School.Grade_calculator(mark)
    