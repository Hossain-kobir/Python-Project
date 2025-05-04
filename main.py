from School_and_Classes import School,Classroom
from person import Teacher,Student
from subject import Subject

High_School=School("Secondary High School","Baradi Bazar")

#make a classroom
Eight=Classroom("Eight")
Nine=Classroom("Nine")
Ten=Classroom("Ten")

#add_classroom_to_school

High_School.add_classroom(Eight)
High_School.add_classroom(Nine)
High_School.add_classroom(Ten)


#adding_teacher
abdul=Teacher("abdul")
kabdul=Teacher("kabdul")
cabdul=Teacher("cabdul")

#adding_Subject

physics=Subject("Physics",abdul)
chemistry=Subject("Chemistry",kabdul)
Biology=Subject("Biology",cabdul)


#adding_subject_to_class

Eight.add_subject(physics)
Eight.add_subject(chemistry)
Eight.add_subject(Biology)

High_School.add_teacher(physics,abdul)
High_School.add_teacher(chemistry,kabdul)

#student_admission_to_class
rahim=Student("Rahim",Eight)
High_School.student_admission(rahim)
kahim=Student("kahim",Eight)
High_School.student_admission(kahim)
mahim=Student("Mahim",Eight)
High_School.student_admission(mahim)

Eight.take_exam()

print(High_School)
