#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Functions
# 
# 
# 

# You’re already familiar with the **print(), input(), and len()** functions from the previous chapters. Python provides several built-in functions like these, but you can also write your own functions. A function is like a mini-program within a program.

# ## What is Function  and Why we need it ?
# 

# ![](../images/unit_6_01.png)

# ### Function Definition
# 
# a function is defined using the **def** keyword followed by the function name, parameter(s) (if any), and a colon : to start the function body. The function body contains the code that is executed when the function is called.

# Syntax :
# 
# ```
# def function_name(parameter1, parameter2, ...):
#     # function body
#     statement1
#     statement2
#     ...
# 
# ```
# 
# 

# To better understand how functions work, let’s create one.

# In[ ]:


def hello(): 
    print('Hello!') 
    print('Hello!!!')
    print('Hello there.')


# In[ ]:


hello()   #  Function call


# In[ ]:


hello() 
hello() 
hello() 


# The **hello()** are function calls. In code, a function call is just the function’s name followed by parentheses, possibly with some number of arguments in between the parentheses. When the program execution reaches these calls, it will jump to the top line in the function and begin executing the code there. When it reaches the end of the function, the execution returns to the line that called the function and continues moving through the code as before.
# 
# A major purpose of functions is to group code that gets executed multiple times. Without a function defined, you would have to copy and paste this code each time, and the program would look like this:

# In[ ]:


print('Hello!')
print('Hello!!!')
print('Hello there.')
print('Hello!')
print('Hello!!!')
print('Hello there.')
print('Hello!')
print('Hello!!!')
print('Hello there.')


# 
# 
# ### def statement with parameters
# 
# When you call the **print()** or **len()** function, you pass in values, called arguments in this context, by typing them between the parentheses. You can also define your own functions that accept arguments.
# 
# 

# In[ ]:


def hello(name):            
    print('Hello '+ name)       


# The definition of the **hello()** function in this program has a parameter called name. A parameter is a variable that an argument is stored in when a function is called.
# 
# 

# In[ ]:


hello('George')
hello('Esra')


# One special thing to note about parameters is that the value stored in a parameter is forgotten when the function returns. For example, if you added **print(name)** after **hello('Esra')** in the previous program, the program would give you a NameError because there is no variable named name. This variable was destroyed after the function call **hello('Esra')** had returned, so **print(name)** would refer to a name variable that does not exist.

# 
# 
# ### Variable Scope and Lifetime

# The **scope of a variable** refers to the part of the program where the variable is visible and can be accessed. It can be divided into two types:

# ### 1 . Local Scope: 
# 
#     Variables declared inside a function have local scope. They are only accessible inside the function and are destroyed when the function completes execution.
# 
# ### 2 . Global Scope:
# 
#     Variables declared outside any function or block have global scope. They are accessible from anywhere in the program, and their lifetime is until the program ends.

# ```{note}
#     **Variable Lifetime:**
#     The lifetime of a variable is the duration for which it exists in the memory.
# ```

# #### Local and Global Variable

# **1 . Local Variable :**
# 
# Local variables have a local scope, meaning they are only accessible within the block of code in which they are defined. This block of code can be a function, a loop, or any other construct that defines a scope.

# In[ ]:


def my_func():
    x = 10  # local variable
    print("Inside my_func(), x =", x)


# In[ ]:


my_func()
print("Outside my_func(), x =", x)  # This will give an error as x is not defined outside the function


# **2 . Global Variable :**
# 
# Global variables, on the other hand, have a global scope, meaning they can be accessed from anywhere in the program. 

# In[ ]:


global_var = 20  # global variable

def my_func():
    local_var = 10  # local variable
    print("Inside my_func(), global_var =", global_var)  # Accessing global variable
    print("Inside my_func(), local_var =", local_var)

my_func()
print("Outside my_func(), global_var =", global_var)


# 
# ### return statement
# 
# 

# When you call the **len()** function and pass it an argument such as ‘Hello’, the function call evaluates to the integer value 5, which is the length of the string you passed it. In general, the value that a function call evaluates to is called the **return value of the function**.
# 
# When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:
# 
# 
# 
# *   The return keyword
# *   The value or expression that the function should return
# 
# 
# 
# 
# 
# When an expression is used with a **return** statement, the **return** value is what this expression evaluates to. For example, the following program defines a function that returns a different string depending on what number it is passed as an argument.

# For example:

# In[ ]:


def areaCircle(r):
  PI=3.14
  result=PI*r*r
  print('The result of circle ')
  return result
areaCircle(5)


# 
# 
# ### Defining Functions with Additional Features
# 
# 

# **1 . Required Arguments :**

# A required argument is an argument that must be provided to a function when it is called. A function that expects a required argument will raise a **TypeError** if the argument is not provided.
# 
# Here's an example of a function with a required argument:

# In[ ]:


def greet(name):
    print("Hello", name)

greet("Alice")  


#  If you don't provide a name argument, you'll get a **TypeError**:

# In[ ]:


greet()


# **2 . Default arguments:** 
# 
# You can specify default values for function arguments, which will be used if the function is called without providing those arguments. For example:

# In[ ]:


def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice") 
greet("Bob", "Hi")  


# **3 . keyword argument :**
# 
# A keyword argument is an argument passed to a function using the argument name, or keyword, as opposed to the order in which the arguments were defined in the function. Keyword arguments allow you to provide default values for function parameters or to specify arguments out of order.
# 
# Here's an example of a function call with keyword arguments:

# In[ ]:


def greet(name, greeting):
    print(greeting , name)

greet(name="Alice", greeting="Hello")
greet(greeting="Hello",name="Alice")


# **4 . Variable-length arguments :**
# 
# You can use "* args"  to pass a variable number of arguments to a function as a tuple, or " **kwargs" to pass a variable number of keyword arguments as a dictionary. For example:

# In[ ]:


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", greeting="Hello")


# 
# 
# ### Lambda or Anonymous Function
# 
# 

# Lambda functions are small, anonymous functions that can be defined inline.
# That means this is function without a name. With normal function we use keyword **def** . But with the lambda function is defined along with the keyword **lambda** . They are often used as arguments to higher-order functions like **map, filter, and reduce**. For example:

# #### 1 . map()

# The map iterator takes a function and applies it to the values in an iterator:

# In[ ]:


numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(list(squares))  


# **2 . filter()**

# The filter iterator looks similar, except it only passes-through values for which the filter function evaluates to True:

# In[ ]:


# find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')


# Note
# 
# The map and filter functions, along with the reduce function (which lives in Python’s functools module) are fundamental components of the functional programming style, which, while not a dominant programming style in the Python world, has its outspoken proponents (see, for example, the (https://toolz.readthedocs.io/en/latest/) library).

# 
# 
# > **Documentation String :**
# 
# A documentation string, also known as a **docstring**, is a string literal that appears as the first statement in a module, function, class, or method definition. The purpose of a docstring is to provide documentation about the code, explaining what it does, how to use it, and any other relevant information.
# 
# Docstrings are enclosed in triple quotes **(''' or """)** and are usually placed immediately after the function or class definition. For example:

# In[ ]:


def my_function(arg1, arg2):
    """ this function is for addition of two numbers
    
    two numbers are read,added and result is displayed."""
    print(my_function.__doc__)

    # Function code goes here
    add = arg1 + arg2
    return add
my_function(1,2)


# **Introduction to Modules and Packages in Python :**
# 
# In Python, a **module** is a file that contains Python code, and a **package** is a directory that contains one or more modules. Modules and packages help in organizing code and make it more reusable.
# 
# Refer this link : [https://realpython.com/python-modules-packages/](https://)

# # **Practice Questions**

# **Difficulty Level : Easy**

# Q. Create a function to calculate the cube of a number that is passed as the argument to the function.
# 
# **Example :**
# 
# def cube(number):
#     ### your code here
# 
# number = 4
# 
# cube(number)
# 
# >>> 64

# In[ ]:


## your code ##


# Q. Create a function to calculate the sum of square of 2 numbers that are defined as the default arguments and its square output is 5.
# 
# **Example :**
# 
# def square(n1 = value,n2 = value):
#     ### your code here
# 
# square()
# 
# >>> 5

# In[ ]:


## your code ##


# Q. Create a function to add two numbers using lambda.

# In[ ]:


## your code ##


# Q. Create a function to calculate the factorial of a number which is passed as an argument and assign the output of the function to a variable named `out`.
# 
# **Example :**
# 
# def factorial(number):
#     ### your code here
# 
# out = factorial(5)
# out
# 
# >>> 120

# In[ ]:


## your code ##


# Q. Correct the syntax of the following function to get the required output.
# 
# **Note** : Make use of all the concepts covered until now.
# 
# **Example :**
# 
# 
# 
# ```
# defn 123string_concatenation{s1 = 'ai',s2 ,s3 = 3);
# 
#     elif s3 == 3;
#     s = s1 + s2 * s3
#         printf[s,end = '-')
#     else;;
#     s = s1 + s2 * 1
#     printf(s,end = '->'\
# 
#     123string_concat{'adventures']
# 
# 
# ```
# 
# 
# 
# 
# 
# >>> 'aiadventuresaiadventuresaiadventures'

# In[ ]:


## your code ##


# Q. Create a function to swap two numbers.
# 
# **Example :**
# 
# def swap(a,b):
# 
#     ### your code here
# a=10,
# b=20
# 
# swap(a,b)
# >>> after swaping a=20,b=10
#   
# 
# 

# In[ ]:


## your code ##


# Q. Create a function for sorting a list of tuples by the second element.
# 
# **Example :**
# 
# my_list = [(2, 3), (1, 2), (4, 1), (3, 4)]
# >>>Output : [(4, 1), (1, 2), (2, 3), (3, 4)]

# In[ ]:





# **Difficulty Level : Medium**

# Q. Write a program to create simple calculator.

# In[ ]:


## your code ##


# Q. Write a program to display the Fibonacci series upto n numbers.

# In[ ]:


## your code ##


# Q. Create a function to calculate the area of triangle or rectangle using 3 arguments : base, height and shape.
# 
# Example :
# 
# def calculate_area(base, height,shape):
#     ### your code here
# 
# b = 2
# h = 6
# 
# calculate_area(b,h, 'Rectangle')
# 
# >>> 12
# 
# 
# calculate_area(b,h, 'Triangle')
# 
# >>> 6.0

# In[ ]:


## your code ##


# Q. Create a function that returns None value and display the result of the string concatenation. You have to take the 2 strings required for the function as argument as shown in the example given below.
# Example :
# 
# def none_value_assignment(s1 = input(),s2 = input()):
#     ### your code here
# 
# var1 = none_value_assignment()
# 
# type(var1)
# 
# >>> result of string concatenation of s1 and s2
# 
# >>> NoneType
# 
# var2 = none_value_assignment('ai', 'adventures')
# 
# type(var2)
# 
# >>> aiadventures
# 
# >>> NoneType

# In[ ]:


## your code ##


# **Difficulty Level : Hard**

# Q. Create a function to calculate and display the sum of the following sequence by taking input from user for n.
# 
# **Sequence** : 1 + 1/1! + 1/2! + 1/3! + + 1/n!
# 
# **Hint** : Give a thought above factorial() you have just created a few problems back.
# 
# def sequence(n):
#     ### your code here
# 
# sequence(5)
# 
# >>> 2.7166666666666663

# In[ ]:


## your code ##


# Q. Create a function to check whether a string is pangram or not.
# 
# **Pangram Definition :** It is a sentence containing all 26 letters of the English alphabets.
# 
# **Example :**
# 
# def ispangram(sentence):
#     ### your code here
# 
# sentence1 = "a quick brown fox jumps over the lazy dog"
# 
# sentence2 = "hello my name is ramesh"
# 
# 
# ispangram(sentence1)
# 
# >>> True
# 
# ispangram(sentence2)
# 
# >>> False

# In[ ]:


## your code ##

