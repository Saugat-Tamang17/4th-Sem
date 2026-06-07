
ages = [18, 20, 19, 21, 22, 18, 20, 23, 21, 19]

# Mean (average) age
mean_age = sum(ages) / len(ages)

# Maximum and Minimum age
max_age = max(ages)
min_age = min(ages)

# Count students above mean age
count_above_mean = 0
for age in ages:
    if age > mean_age:
        count_above_mean += 1

# Display results
print("Ages:", ages)
print("Mean age:", mean_age)
print("Maximum age:", max_age)
print("Minimum age:", min_age)
print("Students above mean age:", count_above_mean)