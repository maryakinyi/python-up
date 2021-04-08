# python strings
# The difference between list and tuples is that tuples are enclosed in parenthesis while list in square brackets.
# tuples indexing and slicing
tuples = (23, 3467, 789, 345, 786)
# INDEXING
print(tuples)
print([3])
# SLICING
print(tuples[:-1])

# List
list1 = [12, 87, 90, "John", 76, "Mary"]
print(list1)
list2 = ["Grace", "Monica"]
print(list2)
# list concatenation
general_list = (list1 + list2)
print(general_list)

genneral_list = list1.extend(list2)
print(general_list)

# list compression
p = []
print(p)
p = [2*x for x in range(5)]
print(p)
p = []
# finding square of a number.
for x in range(5):
    p.append(x**2)
    print(p)
# program to validate if statement is true or false

name = input("whats your name")
if(name=="Mary"):
    print("That name is mine")
else:
    print("I do not know that name")

# Use while loop
add = True
while add == bool:

 ''''taking student details after exams'''''

name = input("Enter name >>>>")
score_in_unit1 = int(input("score in unit1>>>>"))
score_in_unit2 = int(input("score in unit2>>>>"))
score_in_unit3 = int(input("score in unit3>>>>"))
score_in_unit4 = int(input("score in unit4>>>>"))
score_in_unit5 = int(input("score in unit5>>>>"))
score_in_unit6 = int(input("score in unit6>>>>"))
score_in_unit7 = int(input("score in unit7>>>>"))
total = score_in_unit7+score_in_unit6+score_in_unit5+score_in_unit4+score_in_unit3+score_in_unit2+score_in_unit1
print(total)
percentage = (total/900)*100
print(percentage)
print(name, ",your total score is", total, ",your percentage score is", percentage)

