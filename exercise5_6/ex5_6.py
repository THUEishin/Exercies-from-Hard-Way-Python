'''
Exercise 5 and 6 are all about printing format.
In exercise 4, we have the code: print("There are", cars, "cars available")
If there are a lot of variables,such as print(A, "has", B "apples", C, "bannases",...)
then it may be time-wasting to type a lot of "" and ,
So, here comes the format printing

Else, exercises 7,8,9 are all about printing. I will skip them.
'''

#The first type: format syntax
#The second type: f string
my_name = "Ruichen"
x = "My name is {0}."
y = f"My name is {my_name}."
print(x.format(my_name))
print(y)
my_name = "Eishin"
print(x.format(my_name))
#y will not be changed
print(y)