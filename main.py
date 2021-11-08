# calculating average height not using len and sum function
student_height=input("Input a list of student height:").split()
for i in range(0,len(student_height)):
  student_height[i]=int(student_height[i])
print(student_height)
total_height=0
for height in student_height:
  total_height=total_height+height
print(total_height)

number_of_student=0
for student in student_height:
  number_of_student+=1
print(number_of_student)

# Calculating highest score
student_score=input("Input a list of student score:").split()
for i in range(0,len(student_score)):
  student_score[i]=int(student_score[i])
print(student_score)
highest_score=0
for score in student_score:
  if score>highest_score:
    highest_score=score

print(f"The highest score in the class is:{highest_score}")