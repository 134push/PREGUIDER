## the new data structyre in python is list and tuple
## list is mutable and tuple is immutable

## example of list
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list[0] = 10
print(my_list)

## 10 top function used in list
students = ["Pushpam", "Raj"]

students.append("Aman")
print(students)

students.insert(1, "Rahul")
print(students)

students.remove("Raj")
print(students)

students.pop()
print(students) 

students.sort()
print(students)

students.reverse()
print(students)

print(students.index("Rahul"))