'''
This exercise is to read from .txt file
Pay attention to the operations to a file
Namely, close, read, readline, truncate, write("  "), seek(0)
'''

from sys import argv

script, filename = argv
txt = open(filename)

print(f"Here is your file {filename}")
#readline() is to read a line from the file
#strip(*) is to delete the character * at the beginning or end of the string
line = txt.readline().strip(' ').strip('\n')
while line:
    print(line)
    line = txt.readline().strip(' ').strip('\n')
