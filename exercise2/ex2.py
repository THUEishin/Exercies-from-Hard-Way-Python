'''
This exercise is to show how to add comments for python code.
The comment here (at the very beginning of a file) is called 
file comment.
'''
#Also we can use the character(#) to do some comments
import sys
sys.path.append('../')

#I add an empty file (__init__.py) in the exercise1 folder
#Then I can import the file in the folder exercise1 as module
#from the system path (../). Put you mouse on the name (ex1)
#you will see the file comments in the file ex1.py
import exercise1.ex1


#Here, we define a new function
def SayHello():
    '''
    The comment here is called function comment which is used
    to explain the function.
    This function is used to print a Hello_World on the screen.
    '''
    print("Hello World")
    
#If you put your mouse on the following name of the function
#you will see the function comment
SayHello()
