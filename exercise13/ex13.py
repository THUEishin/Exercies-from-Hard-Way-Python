'''
This exercise is to read parameters from command line arguments.
Exercise 14 combines this method with input(), and I will skip it.
'''

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)