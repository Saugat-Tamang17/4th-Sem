student={}
student["Name"]=input("Enter the Name:")
student["Age"]=input("Enter the Age:")
student["Faculty"]=input("Enter the Faculty:")
student["Semester"]=input("Enter the Semester:")

print("\n Student Information:\n")
for key, value in student.items():
  print(f"{key}:{value}")