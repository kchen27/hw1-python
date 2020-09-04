#Author: Kyle Chen kvc5823@psu.edu 

#Course 1 Codes
GradeP1 = input("Enter your course 1 letter grade: ")
CreditP1 = int(input("Enter your course 1 credit: "))
if GradeP1 == "A":
  GradePt1 = 4
  print("Grade point for course 1 is: 4.0")
elif GradeP1 == "A-":
  GradePt1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif GradeP1 == "B+":
  GradePt1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif GradeP1 == "B":
  GradePt1 = 3.0
  print("Grade point for course 1 is: 3.0")
elif GradeP1 == "B-":
  GradePt1 = 2.67
  print("Grade point for course 1 is: 2.67")
elif GradeP1 == "C+":
  GradePt1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif GradeP1 == "C":
  GradePt1 = 2.0
  print("Grade point for course 1 is: 2.0")
elif GradeP1 == "D":
  GradePt1 = 1.0
  print("Grade point for course 1 is: 1.0")
else:
  GradePt1 = 0
  print("Grade point for course 1 is: 0.0")

#Course 2 Codes
GradeP2 = input("Enter your course 2 letter grade: ")
CreditP2 = int(input("Enter your course 2 credit: "))
if GradeP2 == "A":
  GradePt2 = 4
  print("Grade point for course 2 is: 4.0")
elif GradeP2 == "A-":
  GradePt2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif GradeP2 == "B+":
  GradePt2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif GradeP2 == "B":
  GradePt2 = 3.0
  print("Grade point for course 2 is: 3.0")
elif GradeP2 == "B-":
  GradePt2 = 2.67
  print("Grade point for course 2 is: 2.67")
elif GradeP2 == "C+":
  GradePt2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif GradeP2 == "C":
  GradePt2 = 2.0
  print("Grade point for course 2 is: 2.0")
elif GradeP2 == "D":
  GradePt2 = 1.0
  print("Grade point for course 2 is: 1.0")
else:
  GradePt2 = 0
  print("Grade point for course 2 is: 0.0")

#Course 3 Codes     
GradeP3 = input("Enter your course 3 letter grade: ")
CreditP3 = int(input("Enter your course 3 credit: "))
if GradeP3 == "A":
  GradePt3 = 4
  print("Grade point for course 3 is: 4.0")
elif GradeP3 == "A-":
  GradePt3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif GradeP3 == "B+":
  GradePt3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif GradeP3 == "B":
  GradePt3 = 3.0
  print("Grade point for course 3 is: 3.0")
elif GradeP3 == "B-":
  GradePt3 = 2.67
  print("Grade point for course 3 is: 2.67")
elif GradeP3 == "C+":
  GradePt3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif GradeP3 == "C":
  GradePt3 = 2.0
  print("Grade point for course 3 is: 2.0")
elif GradeP3 == "D":
  GradePt3 = 1.0
  print("Grade point for course 3 is: 1.0")
else:
  GradePt3 = 0
  print("Grade point for course 3 is: 0.0")
  
  

GPA = (GradePt1 * CreditP1 + GradePt2 * CreditP2 + GradePt3 * CreditP3)/(CreditP1 + CreditP2 + CreditP3)

print ("Your GPA is:", GPA)
