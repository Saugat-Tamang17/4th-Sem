marks={}

for i in range(5):
  name = input(f"Enter the name of student{i+1}:\t")
  score = int(input(f"Enter the score of student{i+1}:\t"))
  marks[name]=score # creating a key value pair ( dictionary)

  highest_scorer=max(marks,key=marks.get)
  lowest_scorer=min(marks,key=marks.get)

average_marks = sum(marks.values()) / len(marks)

print("\nStudent Marks:", marks)
print("Highest Scorer:", highest_scorer, "with marks", marks[highest_scorer])
print("Lowest Scorer:", lowest_scorer, "with marks", marks[lowest_scorer])
print("Average Marks:", average_marks)