list1 = []
list2 = []
list3 = []

with open("students.csv", "w") as file:
   for line in file:
      row = line.rstrip().split(",")
      list1.append(row[0])
      list2.append(row[1])
      list3.append(row[2])


print(list1)
print(list2)
print(list3)


