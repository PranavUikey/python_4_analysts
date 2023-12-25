#!/usr/bin/env python
# coding: utf-8

# # Expressions

# Play [this](https://www.mathsisfun.com/games/guess_number.html) game before you start programming.

# ![](../images/unit_1_01.png)

# The Python programming language has a wide range of syntactical constructions, standard library functions, and interactive development environment features. Fortunately, you can ignore most of that; you just need to learn enough to write some handy little programs.
# 
# You will, however, have to learn some basic programming concepts before you can do anything. Like any other beginner-in-training, you might think these concepts seem arcane and tedious, but with some knowledge and practice, you’ll be able to command your computer to perform incredible feats.

# ## Literal Constant

# ![](../images/unit_1_02.jpg)

# ### Numeric literal
# 
# ---
# 
# A numeric literal is a sequence of numeric characters that represent a number. There are three types of numeric literals in Python: integers, float numbers, and complex numbers. The numeric literals are immutable i.e. we can not change them.
# 

# 1) Integers: Integers are whole numbers without a decimal point. They can be 
# positive or negative.
# 
# Example:

# In[ ]:


a = 5    # positive integer
b = -10  # negative integer
c = 0    # zero


# 2) Float numbers: Float numbers, also known as floats, are numbers with a decimal point. They can also be positive or negative.

# In[ ]:


a = 3.14      # positive float
b = -2.5      # negative float
c = 1.0e-5   # scientific notation for a very small float (0.00001)


# 3) Complex numbers: Complex numbers consist of a real part and an imaginary part. They are written in the form a + bj, where a is the real part, b is the imaginary part, and j is the imaginary unit.

# In[ ]:


a = 3 + 2j   # a complex number with real part 3 and imaginary part 2
b = 4j       # a complex number with real part 0 and imaginary part 4
c = -1j      # a complex number with real part 0 and imaginary part -1


# Note: In Python, you can use underscores (_) to make large numeric literals easier to read. For example, you can write 1_000_000 instead of 1000000.

# 
# 
# ---
# 
# 
# 
# 
# 
# ### Boolean Literals
# 
# ---
# 
# 

# A boolean literal is a value that can only be one of two possible states: True or False. Boolean literals are used to represent logical values, where True represents a condition that is true or valid, and False represents a condition that is false or invalid.

# In[ ]:


a = True
b = False
print(a==1)
print(b==0)


# Interger value of booleans: value of True is 1 and value of False is 0.

# 
# 
# ---
# ### String Literals
# 
# 
# ---
# 

# A string literal is a sequence of characters enclosed in quotes (either single quotes or double quotes). String literals are used to represent textual data in Python.

# In[ ]:


a = "Hello, World!"     # a string literal enclosed in double quotes
b = 'Python is awesome' # a string literal enclosed in single quotes
number_string = "42"    # a number given in quotes is also a string
data=''                 # an empty string / blank string


# If you ever see the error message **SyntaxError: EOL while scanning string literal**, you probably forgot the final single quote character at the end of the string, such as in this example:

# In[ ]:


'Hello world!


# #### String Concatenation

# The meaning of an operator may change based on the data types of the values next to it. For example, **+** is the addition operator when it operates on two integers or floating-point values. However, when **+** is used on two string values, it joins the strings as the string concatenation operator. Try out the following example.

# In[ ]:


'ai' + 'adventures'


# The expression evaluates down to a single, new string value that combines the text of the two strings. However, if you try to use the + operator on a string and an integer value, Python will not know how to handle this, and it will display an error message.

# In[ ]:


'ai' + 42


# The error message says that python can’t do the operation because python does not knows how to add a str and an int. User has to convert the int to str data type before he/she can add 42 to ‘ai’.

# #### String Replication

# The * operator is used for multiplication when it operates on two integer or floating-point values. But when the * operator is used on one string value and one integer value, it becomes the string replication operator. Enter a string multiplied by a number to see this in action.

# In[ ]:


'ai'*5


# The expression evaluates down to a single string value that repeats the original a number of times equal to the integer value. String replication is a useful trick, but it’s not used as often as string concatenation.
# 
# The * operator can be used with only two numeric values (for multiplication) or one string value and one integer value (for string replication). Otherwise, Python will just display an error message.
# 
# For example …

# In[ ]:


'ai' * 'adventures'


# In[ ]:


'ai' * 5.0


# 
# 
# ---
# ### Special Literals
# 
# 
# ---
# 

# "special literals" refer to predefined values that have their own data type and special meaning. 
# 
# None: This represents the absence of a value. It is often used as a placeholder or to indicate that a variable has not been assigned a value yet.

# In[ ]:


x = None 
x        # here there is no any value in x 


# ## Variables

# A **variable** is like a envelope in the computer’s memory where you can store a single value. If you want to use the result of an evaluated expression later in your program, you can save it inside a variable.
# 
# **Assignment Statements**
# 
# You’ll store values in variables with an assignment statement. An assignment statement consists of a variable name, an equal sign (called the assignment operator), and the value to be stored. If you enter the assignment statement **var = 42**, then a variable named var will have the integer value 42 stored in it.
# 
# Think of a variable as a labeled envelope that a value is placed in, as in the figure.

# ![](../images/unit_1_03.png)

# In python, a variable is initialized (or created) the first time a value is stored in it

# In[ ]:


var = 40
var


# ```{note}
# 
# Here we are not using print() function but still it displays the output. This is only possible in Jupyter Notebook, every last line of code cell always displays the output of the variable or operation. If you want to see the output intermediately then use print() function.
# ```

# You can use variables which are already initialized in expressions with other variables.

# In[ ]:


balls = 2
print(var + balls)
var + balls + var


# When a variable is assigned a new value, the old value is forgotten, which is why var evaluated to 42 instead of 40 at the end of the example. This is called overwriting the variable. Try the following code into your Jupyter Notebook’s cell to overwriting a string:
# 
# 

# In[ ]:


var = var + 2
var


# In[ ]:


var = 'Hello'
var


# In[ ]:


var = 'Goodbye'
var


# ![image.png](data:image/png;base64,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)

# ### Rules for variable names

# Variable Names
# Table below has examples of legal variable names. You can name a variable anything as long as it obeys the following three rules:
# 
# *   It can be only one word.
# *   It can use only letters, numbers,  and the underscore (_) character.
# 
# 
# *   It can’t begin with a number.
# 
# 
# 
# 

# ![](../images/unit_1_05.jpg)

# Another important thing to note, variable names are case-sensitive, meaning that **var**, **VAR**, **Var**, and **vAr** are four different variables. It is a Python convention to start your variables with a lowercase letter.
# 
# A good variable name describes the data it contains. Imagine that you moved to a new house and labeled all of your moving boxes as stuff. You’d never find anything! The variable names var, balls, and pencils are used as generic names for the examples, but in your programs, a descriptive name will help make your code more readable.

# ## Arithmatic Operators

# ![](../images/unit_1_06.jpg)

# In[ ]:


5+2  # addition


# In[ ]:


5-2  # subtraction


# In[ ]:


5*2  # multiplication


# In[ ]:


5/2  # true division


# In[ ]:


5//2  # floor division


# In[ ]:


5%2 # modulus


# In[ ]:


5**2  # exponention


# ## Your First Program

# Lets write our first program. This is a pretty simple program. It will say hello and then ask the user to enter his/her name & age.
# 
# You should write the following code in your jupyter notebook and try running it.
# 
# ```{note}
# Don’t worry a lot about understanding the complete code. We will be discussing it in detail.
# ```

# In[ ]:


# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# ### Comments

# The following line is called a *comment*.

# In[ ]:


# This program says hello and asks for my name.


# Python ignores comments, and you can use them to write notes or remind yourself what the code is trying to do. Any text for the rest of the line following a hash mark (#) is part of a comment. This means, for example, that you can have stand-alone comments like the one just shown, as well as inline comments that follow a statement. For example:

# In[ ]:


print('What is your name?')    # ask for their name


# Sometimes, programmers will put a “#” in front of a line of code to temporarily remove it while testing a program. This is called commenting out code, and it can be useful when you’re trying to figure out why a program doesn’t work. You can remove the “#” later when you are ready to put the line back in.

# 
# 
# ### `print()` function
# 
#   The print() function displays the string value inside the parentheses on the screen.
# 
# 

# In[ ]:


print('Hello world!')

print('What is your name?') # ask for their name


# The line print('Hello world!') means “Print out the text in the string ‘Hello world!’.”
# 
#  Notice that the quotes are not printed to the screen. They just mark where the string begins and ends; they are not part of the string value.

# ```{note}
# 
# You can also use this function to put a blank line on the screen; just call print() with nothing in between the parentheses.
# 
# ```

# 
# 
# ### `input()` function
#   The input() function waits for the user to type some text on the keyboard and press ENTER.
# 
# 
# 

# In[ ]:


myName = input()


# This function call evaluates to a string equal to the user’s text, and the previous line of code assigns the myName variable to this string value.
# 
# You can think of the **input()** function call as an expression that evaluates to whatever string the user typed in. If the user entered ‘Ram’, then the expression would evaluate to **myName = 'Ram'**.

# 
# 
# ### Printing the user’s name
# 
#   The following call to print() actually contains the expression 'It is good to meet you, ' + myName between the parentheses.
# 
# 
# 
# 
# 
# 

# In[ ]:


print('It is good to meet you, ' + myName)


# Remember that expressions can always evaluate to a single value. If ‘Ram’ is the value stored in myName on the previous line, then this expression evaluates to 'It is good to meet you, Ram'. This single string value is then passed to print(), which prints it on the screen.

# ```{note}
# 
# The `input()` function always returns a string, even if the user enters a number.
# 
# Enter `user_value = input() into the cell and enter 101 when it waits for your text.
# 
# ```

# In[ ]:


user_value = input()


# In[ ]:


user_value


# ### `len()` function
# 
# 

# You can pass the **len()** function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

# In[ ]:


print('The length of your name is:')
print(len(myName))


# In[ ]:


len('hello')


# In[ ]:


len('I am data analyst')


# In[ ]:


len('')


# Just like those examples, **len(myName)** evaluates to an integer. It is then passed to **print()** to be displayed on the screen. Notice that **print()** allows you to pass it either integer values or string values. But notice the error that shows up when you type the following into the cell:

# In[ ]:


print('I am ' + 24 + ' years old.')


# The print() function isn’t causing that error, but rather it’s the expression you tried to pass to print(). You get the same error message if you type the expression into the cell on its own.

# In[ ]:


'I am ' + 24 + ' years old.'


# Python gives an error because you can use the + operator only to add two integers together or concatenate two strings. You can’t add an integer to a string because this is ungrammatical in Python. You can fix this by using a string version of the integer instead, as explained in the next section.

# ### `str()` function
# 
#   If you want to concatenate an integer such as 24 with a string to pass to print(), you’ll need to get the value '24', which is the string form of 24. The str() function can be passed an integer value and will evaluate to a string value version of it, as follows:
# 
# 

# In[ ]:


str(24)


# In[ ]:


print('I am ' + str(24) + ' years old.')


# Because **str(24)** evaluates to ‘24’, the expression **'I am ' + str(24) + ' years old.'** evaluates to **'I am ' + '24' + ' years old.'**, which in turn evaluates to 'I am 24 years old.'. This is the value that is passed to the print() function.
# 
# The str() function is handy when you have an integer or float that you want to concatenate to a string.

# ### `int()` function
# 
#   The value stored inside **user_value** isn’t the integer **101** but the string **'101'**. If you want to do math using the value in user_value, use the **int()** function to get the integer form of user_value and then store this as the new value in user_value.
# 
# 

# In[ ]:


user_value = int(user_value)
user_value


# Now you should be able to treat the user_value variable as an integer instead of a string.

# In[ ]:


user_value *10/5


# ```{note}
# 
# If you pass a value to `int()` that it cannot evaluate as an integer, Python will display an error message.
# 
# ```

# In[ ]:


int('99.99')


# In[ ]:


int('twelve')


# ### `float()` function
#  
#   Float values are those which contains decimal points. Let’s take the another example of my_value containing string'84' and you want it in float type, then use float() to get in floating point number and store in another variable.
# 
# 

# In[ ]:


my_value = input()


# In[ ]:


my_value = float(my_value)
my_value


# In your program, you used the **int()** and **str()** functions in the last three lines to get a value of the appropriate data type for the code.

# In[ ]:


print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# The myAge variable contains the value returned from input(). Because the input() function always returns a string (even if the user typed in a number), you can use the int(myAge) code to return an integer value of the string in myAge. This integer value is then added to 1 in the expression int(myAge) + 1.
# These evaluation steps would look something like this:

# ![](../images/unit_1_07.png)

# 
# 
# ---
# 
# 
# ## Data Types
# 
# 
# ---
# 
# 

# ![](../images/unit_1_08.jpg)

# We already saw Numeric, Strings & Boolean data types now we will start with other data types:

# 
# 
# ### Lists
# 

# a list is a built-in data type that represents a collection of items, which can be of any data type. A list is an ordered sequence of elements, where each element is identified by an index starting from 0.
# 
# Lists are created using square brackets [ ] and separating each element with a comma. For example, here's how you can create a list of numbers:

# In[ ]:


numbers = [1, 2, 3, 4, 5]
my_list = ["apple", 3, True, [5, 6, 7]]   # Lists can also contain elements of different data types


# 
# 
# ### Tuples
# 
# 

# a tuple is a built-in data type that is similar to a list, but with some important differences. Like a list, a tuple is an ordered collection of elements, where each element can be of any data type.
# 
# Tuples are immutable which means that once they are created, their contents cannot be changed

# In[ ]:


my_tuple = ("apple", 3, True)


# 
# 
# ### Dictionary
# 
# 

# a dictionary is a built-in data type that represents a collection of key-value pairs. The keys in a dictionary are unique and immutable, and each key is associated with a value.
# 
# Dictionaries are created using curly braces { }, with each key-value pair separated by a colon : and individual pairs separated by commas. For example:

# In[ ]:


student_ages = {"Alice": 20, "Bob": 19, "Charlie": 21}
print(student_ages)
print(student_ages["Alice"])  # Output: 20


# ### Sets
# 
# 

# In[ ]:


# Create a set
my_set = {1, 2, 3, 4, 5}

# Print the set
print(my_set)


# 
# 
# ## Definition of an Expression
# 
# 
# An expression is a combination of values, variables, and operators that Python interprets and evaluates to a result. Python expressions can be simple, such as a single variable, or complex, such as a combination of variables, operators, and function calls.
# 
# Here are some examples of simple expressions in Python:

# In[ ]:


x = 10        # variable assignment
y = 5         # variable assignment
z = x + y     # addition operator
z


# In[ ]:


2 + 3 *4


# 
# 
# ## Practice Questions
# 
# 

# ### Difficulty Level : Easy

# Q. Add parentheses to the following expression so that it evaluates to 0. 
# 
# 8 - 3 * 2 - 1 + 1

# In[ ]:


## your code ##


# Q. Implement Simple Interest Formula : **S.I. = P × R × T**
# 
# 
# 
# *   P = 1500
# *   R = 9.5
# 
# *   T = 20
# 
# 
# 
# 
# 
# 
# 

# In[ ]:


## your code ##


# Q. Try to implement Compound Interest Formula : **V = P(1+r/n)^nt**
# 
# 
# *   P = 1500
# *   r = 0.043
# 
# *   n = 4
# *   t = 6
# 
# 
# 
# 
# 
# 

# In[ ]:


## your code ##


# Q. Calculate Momentum is calculated as **e=mc^2** 
# 
# where **m** is the mass of the object and **c** is its velocity.

# In[ ]:


## your code ##


# Q. Implement Fahrenheit to Celsius conversion formula : **F = ( C x 9 / 5 ) + 32**
# 
# 
# *   C = 253
# 
# 

# In[ ]:


## your code ##


# ### Difficulty Level : Medium

# Q. Create 2 variables and assign values like name and surname from the user. Then concatenate these 2 variables and display using print function.

# In[ ]:


## your code ##


# Q. Create 2 variables and assign values like birth month and birth year from the user. Display these 2 variables and the length of these variables inside a single print function.

# In[ ]:


## your code ##


# ### Difficulty Level : Hard

# Q. Create 2 variables and assign values of user's favourite IPL team and any number between 1 - 10. Display the name of this favourite IPL team as many times as the number they pick from 1 - 10.
# 
# **Note** : Pass the message in the input function for taking information from the user.

# In[ ]:


## your code ##


# Q. Create 4 variables and take input from user for information like height, weight, age and a number from 1 - 10. Display the results of true division, floor division and exponentiation of height, weight and age with the number selected from 1 - 10 concatenated together inside a print function respectively.
# 
# **Note** : Pass the message in the input function for taking information from the user. 
# 
# **Hint** : Concatenate string \n to display output on new line.

# In[ ]:


## your code ##


# Q. Calculate salary of employee given his basic pay (take as input from user). Calculate gross salary of employee. Let HRA be 10% of basic pay and TA be 5% of the basic pay. Let employee pay professional tex as 2% of total salary. Calculate net salary payable after deductions.

# In[ ]:


## your code ##

