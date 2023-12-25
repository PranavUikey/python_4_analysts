#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Loops
# 
# 

# A loop is a construct that allows a set of instructions to be repeated multiple times until a certain condition is met.
# 
# 
# *   Iteration is a technique that allows to execute a block of statements repeatedly.
# *   **Definition :** Repeated execution of a set of statements is called **iteration**.
# *  The programming constructs used for iteration are while , for , break , continue and so on .
# 
# Let us discuss the iteration techniques with the help of illustrative examples.
# There are several types of loops:
# 
# 
# 
# 

# 
# 
# ## while loop
# 
# 

# A while loop is a type of control flow statement in programming that allows a piece of code to be executed repeatedly as long as a certain condition is true.
# 
# The condition in the while loop is evaluated before each iteration of the loop. If the condition is true, the code inside the loop is executed. This process continues until the condition becomes false, at which point the loop terminates and control passes to the next statement in the program.
# 
# Here's an example of a simple while loop in Python that prints the numbers from 1 to 5:

# In[ ]:


i = 1           # iniialization
while i <= 5:   # condition
    print(i)
    i += 1      # increment


# In this example, the loop starts with i equal to 1, and the condition is that i is less than or equal to 5. Inside the loop, the value of i is printed and then incremented by 1. The loop continues to execute until i becomes 6, at which point the condition becomes false and the loop terminates. The output of this program would be:

# Let’s take an example of while loop which will print all numbers divisible by 5 starting from 10 to 20.
# 

# In[ ]:


x = 10          # initialize `x` at 10 because our starting point is 10
while  x <= 20: # condition to check till `x` becomes 20
  if x % 5 ==0: # condition to check the number divisible by 5.
    print(x)
  x=x+1         # increment `x` by 1 (The short version of writing the same thing is x+=1) )


# We can do the same thing in reverse order by changing the values like following code:

# In[ ]:


x = 20
while x >= 10:
  if x % 5 == 0:
    print(x)
  x=x-1


# ```{question}
# 
# Now try out the same example for even numbers without if statement (in ascending and descending order).
# ```

# ```{note}
# If you forget any of the steps in while loop it will stuck in infinite loop, which we will cover later in this chapter.
# ```

# 
# 
# ## range() function
# 
# 
# 
# 
# 
# 

# Some functions in python can be called with multiple arguments separated by a comma, and range() is one of them. range() function creates a sequence of integers, for that we have to mention following things:
# 
# 
# 
# *   start - The number from where sequence will start, its just like initialization from while loop. 
# *   stop - The number where the sequence will end, just like the condition of while loop to stop the loop.
# *   step- The number which tells how much differene will be between next valud of the sequence, increment/decrement from while loop.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# So if you remember we have mentioned in the start of the lesson those 3 properties of loops being used by for loop but in quite different way with the help of range() function.
# 
# The general syntax of **range()** function is : `range(start, stop, step)`

# In[ ]:


range(1, 5, 1)


# The above code is not giving us the output because in Python 3 range() won’t display the complete sequence of integers. Hence we need for loop which will iterate over this sequence and display every element of the sequence until it ends. Let’s use the same sequence as above and create a for loop.

# 
# 
# ## for loop
# 
# 

# A for loop is a programming construct that allows you to iterate over a collection of items or perform a set number of iterations.

# In[ ]:


for i in range(1, 5, 1):
  print(i)


# ```{note}
# 
# *Stop argument* - Always remember it is excluded from the sequence. If you want the sequence from 0 to 10 both numbers included then your range() should be like range(0,11,1).
# ```

# In[ ]:


for i in range(1, 6):
  print(i)


# Now what’s happenning in the above code is we are mentioning the start as 1 and stop as 6 (i.e.- the sequence will become 1, 2, 3, 4, 5), and we haven’t mentioned step so it automatically take it value as +1.

# ```{note}
# 
# *Step argument*  - Step is to tell the difference between two consecutive numbers of the sequence. For example range(1,5,1) the step is +1 means increment. By default the value of step is +1 even if you didn’t provide it’s value it will be +1.
# 
# ```

# In[ ]:


for i in range(6):
  print(i)


# In above code we haven’t mentioned start and step argument both. The only value we have provided is stop. And it automatically starts from 0.

# ```{note}
# 
# *Start argument* - Start is to tell range from where the sequence should start. By default it’s value is 0, means if you don’t provide the start number it will automatically start from 0 as shown above.
# 
# ```

# ```{question}
# 
# 
# Now try to create a sequence from 5 to 1.(Hint - It has something to do with step).
# ```

# As we have written a code for numbers divisible by 5 using while loop, we can do it using for loop too. As shown below:

# In[ ]:


for x in range(10, 21): # stop value will be 21 because 20 should get included in the sequence
  if x % 5 == 0:
    print(x) 


# This example shows the similarity between for and while loop. If you know the end point or stopping point of the loop you can use both the loops.
# 
# But if you have to repeat something until some condition is False and you don’t know how many times the loop should repeat itself, then go with while loop.

# ```{question}
# 
# Now try out the for even numbers without if statement (in ascending and descending order) using for loop.
# ```

# 
# Till now you have seen that both the loops only gets over when it reaches its stopping point/condition.
# 
# But we can stop the loop before it reaches it’s stopping point/condition. by mentioning break statement.

# 
# 
# 
# ---
# 
# 
# ## break statement :
# 
# 
# 
# ---
# 
# 

# break statement helps you stop any loop before it reaches it stop point. you just have to write break as shown below.

# In[ ]:


for i in  range(1,6):
  if i ==4:
    break
  print(i, end = ' ')


# 
# 
# ---
# 
# 
# 
# ---
# 
# 
# ## continue statement
# 
# ---
# 

# continue is opposite of break statement. continue statement will skip the loop to next value when the mentioned condition arises and go on until the loop reaches its stop point. Let’s understand it using code below.

# In[ ]:


for i in range(1,6):
  if i==3:
    continue
  print(i, end = ' ')


# 
# 
# ## Types of loops:
# 
# 

# ### 1 . Nested Loops
# 
# Nested term in programming is used to show one thing is inside the other. Here we are using the term nested loop, it means one loop inside the other. for example while loop inside another while loop or for loop inside another for loop or for loop inside while loop or vice versa. Let’s understand it using few examples:

# In[ ]:


for i in range(3):
  for j in range(3):
    print(i,j)


# Now if you look closely you will observe that unless until the loop which is inside is gets over the outer loop won’t increment to next value. In simple word nexted loop acn be used to create possible combination of numbers.

# ```{question}
# 
# Now try the same thing with while loops.
# 
# ```

# ### 2 . Infinite Loop
# 
#  It is a loop which will go on until you explicitly break the loop. Usually infinte loop is created with while loop. Most of the time it could happen with you because you loop couldn’t reach it’s stop point. If it happens with you can just stop the execution by interrupting the runtime from google colab’s runtime section. 

# In[ ]:


i = 0
while i<=5:
  print(i)


# ### 3 . for-else loop
# 
# In Python, for-else loop is a variation of the for loop. It has an optional else block that gets executed after the loop completes, but only if the loop completes normally (i.e., without encountering a break statement).

# Here's the syntax for a for-else loop in Python:
# 
# 
# 
# 
# 
# ```{python}
# for variable in sequence:
#     # Code to be executed in each iteration
# else:
#     # Code to be executed after the loop completes normally
# 
# ```
# 
# 
# 
# 

# Here's an example of a for-else loop in Python that uses the range function to loop through a sequence of numbers and prints a message when the loop completes:

# In[ ]:


for i in range(5):
    print(i)
else:
    print("Loop completed normally")


# ### 4 . while-else loop
# 
# It is possible to include an "else" clause after a "while" loop. This code will execute if the loop terminates normally (i.e., if the condition in the "while" statement becomes false).
# 
# For example:

# In[ ]:


x = 0
while x < 10:
    print(x)
    x = x + 1
else:
    print("x is now greater than or equal to 10")


# ### 5 . `pass` keyword
# 
# The `pass` keyword is a way to indicate that you want to do nothing in a certain block of code. It can be useful as a placeholder when you're working on code and haven't yet implemented a certain section.
# 
# For example, in a loop where you want to perform some action if a certain condition is true, but do nothing if the condition is false, you could use the `pass` keyword to indicate that nothing should be done in the `else` block:

# In[ ]:


for i in range(5):
    if i == 4:
      pass
      print('reached at pass statement')
    print(i)


# In[ ]:





# 
# 
# ## Pre-test loop and Post-test loop 
# 
#   In Python, a pre-test loop (also called a "while loop") and a post-test loop (also called a "do-while loop") can be implemented using the following code structures:
# 
# 

# 
# 
# ### 1 . Pres-test(while loop) 
# 
# The loop will continue to run as long as the condition is true. Here's an example that prints out the numbers 1 to 5 using a pre-test loop:
# 
# 

# In[ ]:


i = 1
while i <= 5:
    print(i)
    i += 1


# 
# 
# ### 2 . Post-test loop (do-while loop)
# 
# The loop will run at least once before checking the condition. If the condition is true, the loop will continue to run, otherwise it will exit. Here's an example that asks the user to enter a number between 1 and 10, and keeps asking until a valid number is entered:
# 

# In[ ]:


while True:
    num = int(input("Enter a number between 1 and 10: "))
    if num >= 1 and num <= 10:
        break
print("You entered:", num)


# ## Practice Questions

# ### Difficulty Level : Easy

# Q. Create a program to display the first 10 even numbers in reverse order in a single line using end parameter of print function.
# 
# **Note** : Use both the loops.
# 
# 

# In[ ]:


## your code ##


# Q. Create a program that displays numbers starting from 20 to 40 with a difference of 5 in a single line using end parameter of print function.
# 
# **Note** : Use both the loops.

# In[ ]:


## your code ##


# Q. Create a program to display the cube of first 5 numbers in single line using end parameter of print function.
# 
# **Note** : Use both the loops.
# 
# 

# In[ ]:


## your code ##


# Q. Create a program to display the factorial of a number.
# 
# **Note** : Use both the loops with positive and negative step values.

# In[ ]:


## your code ##


# ### Difficulty Level : Medium

# Q. Create a program that keeps on accepting input from user until 0 is entered and print the sum of all the numbers entered at the end.
# 

# In[ ]:


## your code ##


# Q. Create a program to print the following series for `n` terms where `n` is the number taken from the user.
# 
# **Series** : 2,22,222,2222,...... n terms

# In[ ]:


## your code ##


# Q. Create a program to print factorial of given number.
# 
# for example:       n=5
# 
# output: factorial of 5 is 120.

# In[ ]:


## your code ##


# 
# ### Difficulty Level : Hard

# Q. Create a program to print all prime numbers from 0 to limit. Take limit as input.

# In[ ]:


## your code ##


# Q. Create a program that displays the first number divisible by 5 between 6 to 16 and then break the loop.
# 
# **Note** : Use both the loops.

# In[ ]:


## your code ##


# Q. Create a program that replicates the following output :
# 
# **Note** : Use both the loops.
# 
# The Multiplication Table of 2
# 
# 2 x 1 = 2
# 
# .
# 
# .
# 
# .
# 
# The Multiplication Table of 3
# 
# 3 x 1 = 3
# 
# .
# 
# .
# 
# .
# 
# The Multiplication Table of 4
# 
# 4 x 1 = 4
# 
# .
# 
# .
# 
# .

# In[ ]:


## your code ##


# Q. To check whether input number is **Armstrong number** or not . An **Armstrong number** is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. 

# In[ ]:


## your code ##

