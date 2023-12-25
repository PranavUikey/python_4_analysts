#!/usr/bin/env python
# coding: utf-8

# 
# 
# 
# # Strings
# 
# 
# 
# 

# ![](../images/unit_7_01.png)

# We already seen String data type in 1st unit now we will cover some Python's built-in string methods and formatting operations.
# 
# As we know Strings are :
# 
# 
# 1.   Ordered sequences of characters
# 2.   Immutable, which means that once a string is created, its contents cannot be changed.
# 
# Slicing and indexing of strings is just like lists and tuples.
# 

# In[ ]:


language = 'python'


# In[ ]:


language[0]


# In[ ]:


language[0:5]


# In[ ]:


language[-2]


# In[ ]:


language[-4:-2]


# 
# 
# ## String Formatting operator
# 
# 

# String formatting operators are used in Python to format strings by replacing placeholders with values. The % operator is used for string formatting and is often referred to as the "string formatting operator".
# 
# The basic syntax of the string formatting operator is as follows:
# 
# 
# ```
# formatted_string = "format string % (value1, value2, ...)"
# 
# ```
# 
# 

# Here's an example of using the string formatting operator:

# In[ ]:


name = "John"
age = 25
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)


# In addition to the string formatting operator, Python also provides the format() method for string formatting. This method is more flexible and easier to read than the string formatting operator, and is recommended for most cases.
# 
# Here's an example of using the format() method:

# In[ ]:


name = "John"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)


# Various format specifiers are enlisted in the following table:

# ![](../images/unit_7_02.png)

# 
# 
# ## Built in String Methods and Functions
# 
# 

# ![](../images/unit_7_03.png)

# 
# 
# ### Adjusting case
# 
# 

# Python makes it quite easy to adjust the case of a string. Here we’ll look at the upper(), lower(), capitalize(), title(), and swapcase() methods, using the following messy string as an example:

# In[ ]:


line = "i LoVe dATA SciEnCE"


# In[ ]:


line.upper()


# In[ ]:


line.lower()


# A common formatting need is to capitalize just the first letter of each word, or perhaps the first letter of each sentence. This can be done with the title() and capitalize() methods:

# In[ ]:


line.title()


# In[ ]:


line.capitalize()


# The cases can be swapped using the swapcase() method:

# In[ ]:


line.swapcase()


# 
# ### Adding spaces 
# 
# 

# The opposite of this operation, adding spaces or other characters, can be accomplished using the center(), ljust(), and rjust() methods.
# 
# For example, we can use the center() method to center a given string within a given number of spaces:

# In[ ]:


line = "this is the content"
line.center(30)


# Similarly, ljust() and rjust() will left-justify or right-justify the string within spaces of a given length:

# In[ ]:


line.ljust(30)


# In[ ]:


line.rjust(30)


# All these methods additionally accept any character which will be used to fill the space. For example:

# In[ ]:


'435'.rjust(10, '0')


# Because zero-filling is such a common need, Python also provides zfill(), which is a special method to right-pad a string with zeros:

# In[ ]:


'435'.zfill(10)


# 
# 
# ### Removing spaces (strip)
# 
# 

# Another common need is to remove spaces (or other characters) from the beginning or end of the string. The basic method of removing characters is the strip() method, which strips whitespace from the beginning and end of the line:

# In[ ]:


line = '         this is the content         '
line.strip()


# To remove just space to the right or left, use rstrip() or lstrip() respectively:

# In[ ]:


line.rstrip()


# In[ ]:


line.lstrip()


# To remove characters other than spaces, you can pass the desired character to the strip() method:

# In[ ]:


num = "000000000000435"
num.strip('0')


# 
# 
# ### Finding substrings
# 
# 

# If you want to find occurrences of a certain character in a string, the find()/rfind(), index()/rindex(), and replace() methods are the best built-in methods.
# 
# find() and index() are very similar, in that they search for the first occurrence of a character or substring within a string, and return the index of the substring:

# In[ ]:


line = "i love data science"
line.find('data')


# In[ ]:


line.index('data')


# In[ ]:


line.rfind('a')


# For the special case of checking for a substring at the beginning or end of a string, Python provides the startswith() and endswith() methods:

# In[ ]:


line.endswith('science')


# In[ ]:


line.startswith('Me')


# 
# 
# ### Replacing substrings
# 
# 

# To go one step further and replace a given substring with a new string, you can use the replace() method. Here, let’s replace “data science” with “aiadventures”:

# In[ ]:


line.replace('data science', 'aiadventures')


# The replace() function returns a new string, and will replace all occurrences of the input:

# In[ ]:


line.replace('a', '--')


# 
# 
# ### Partitioning strings
# 
# 

# If you would like to find a substring and then split the string based on its location, the partition() method is what you’re looking for. It will return a sequence of substrings.
# 
# The partition() method returns a tuple with three elements: the substring before the first instance of the split-point, the split-point itself, and the substring after.

# In[ ]:


line.partition('data')


# 
# 
# ### Split strings
# 
# 

# The split() method is perhaps more useful; it finds all instances of the split-point and returns the substrings in between. The default is to split on any whitespace, returning a list of the individual words in a string:

# In[ ]:


line.split()


# A related method is splitlines(), which splits on newline characters. Let’s give it a try …

# In[ ]:


motivation = """Fear of failure is higher when you're not working on the problem. 
If you are taking action, you are less worried about failure, 
Because you realize you can influence the outcome."""

motivation.splitlines()


# ### joining strings

# Note that if you would like to undo a split(), you can use the join() method, which returns a string built from a splitpoint and an iterable:
# 

# In[ ]:


'--'.join(['1', '2', '3'])


# A common pattern is to use the special character "\n" (newline) to join together lines that have been previously split, and recover the input:

# In[ ]:


print("\n".join(["Fear of failure is higher when you're not working on the problem.", 
                 'If you are taking action, you are less worried about failure, ', 
                 'Because you realize you can influence the outcome.']))


# There are many more methods in string manipulation. You can refer the link to praactice more methods. link : https://realpython.com/python-strings/#built-in-string-methods
# 

# 
# 
# ### Iterating Strings
# 
# 

# In[ ]:


msg='Goodbye'
for i in range(len(msg)):
  print(i,msg[i])


# We can traverse the string using while loops too:

# In[ ]:


msg='Goodbye'
i=0
while i<len(msg):
  print(i,msg[i])
  i += 1


# 
# 
# ### ord() and chr() Functions :**
# 
# 

# In Python, the ord() and chr() functions are used to convert between characters and their corresponding Unicode code points.
# 
# The ord() function takes a single character as an argument and returns the Unicode code point of that character as an integer. For example:

# In[ ]:


ord('&')


# In[ ]:


ord('a')


# The chr() function takes an integer representing a Unicode code point and returns the corresponding character as a string. For example:

# In[ ]:


chr(97)


# In[ ]:


chr(89)


# 
# 
# ## Comparing Strings
# 
# 

# ![](../images/unit_7_04.png)

# In Python, you can compare strings using comparison operators like **== (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal to), and >= (greater than or equal to)**.
# 
# When comparing strings, Python compares them lexicographically, which means it compares the ASCII or Unicode code point values of each character in the strings, starting from the leftmost character and moving towards the right. If two characters differ, the comparison is determined by the difference between their code point values.

# In[ ]:


'apple' == 'apple'


# In[ ]:


'apple' != 'banana'


# In[ ]:


'cat' < 'dog'


# In[ ]:


'hello' >= 'goodbye'


# 
# 
# ## String Module
# 

# 
# 
# The string module in Python provides a collection of constants and helper functions for working with strings. Some of the most commonly used features of the string module are:
# 
# 1.string.ascii_letters: A string containing all the ASCII letters, both uppercase and lowercase.
# 
# 2.string.digits: A string containing all the ASCII digits.
# 
# 3.string.punctuation: A string containing all the ASCII punctuation characters.
# 
# 4.string.whitespace: A string containing all the ASCII whitespace characters (space, tab, newline, etc.).
# 
# 5.string.capwords(s): A function that capitalizes the first letter of each word in a string.
# 
# Here are some examples of using the string module:

# In[ ]:


import string

# Print all the ASCII letters
print(string.ascii_letters)

# Print all the ASCII digits
print(string.digits)

# Print all the ASCII punctuation characters
print(string.punctuation)

# Print all the ASCII whitespace characters
print(string.whitespace)

# Capitalize the first letter of each word in a string
s = "the quick brown fox jumps over the lazy dog"
print(string.capwords(s))


# Here is the official Python documentation for the string module:
# 
# https://docs.python.org/3/library/string.html
# 
# The documentation provides a comprehensive list of all the constants and functions available in the string module, along with examples of how to use them. It's a great resource for learning more about the string module and how to work with strings in Python.

# ## Practice Questions

# ### Difficulty Level : Easy

# Q. Create a function that checks whether a word or phrase is palindrome or not.
# 
# **Palindrome Definition :** It is a word or sequence that when read from right-to-left or left-to-right mean the same word. Example: madam, kayak, racecar, etc. **Note :** Try solving this using **String Slicing** and **String Concatenation**
# 
# **Example :**
# 
# def palindrome(string):
#     ### your code here
# 
# palindrome('madam')
# >>> 'Palindrome!'
# 
# palindrome('aiadventures')
# >>> 'Not Palindrome!'

# Q. Create a function that splits the string and stores the word and length of the word in a dictionary using dictionary comprehension.
# 
# **Note** : Use String method as well as Regex method.
# 
# **Example :**
# 
# def len_words(string):
#     ### your code here
# 
# string1 = "Practice Problems to Drill List Comprehension in Your Head."
# len_words(string1)
# 
# >>> {'Practice': 8, 'Problems': 8, 'to': 2, 'Drill': 5, 'List': 4, 'Comprehension': 13, 'in': 2, 'Your': 4, 'Head.': 5}

# In[ ]:


## your code ##


# Q. Create a function that partitions the string on **Python** and changes all the uppercase elements to lowercase and vice versa for the 1st part of the partition and capitalizes the words of the 2nd part of the partition.
# 
# **Note** : Use **String** methods.
# 
# **Example :**
# 
# def sentence_partition(string):
#     ### your code here
# 
# string1 = "Students put efforts in learning Python for a successful future in emerging technologies!"
# len_words(string1)
# 
# >>> 'sTUDENTS PUT EFFORTS IN LEARNING Python For A Successful Future In Emerging Technologies!'
# 

# Q. Create a function that takes your full name as argument and returns the abbreviations of the first and middle names except the last name which is displayed as it is.
# 
# 
# **Example :**
# 
# def create_abbreviations(fullname):
#     ### your code here
# 
# name = input('Enter your full name : ')
# create_abbreviations(name)
# 
# >>> 
# Enter your full name : Steve Paul Jobs
# 
# >>>**'S.P.Jobs'**

# ### Difficulty Level : Medium

# Q. Create a function that takes a list of words & returns the lenght of the longest one.
# list1=['Vivek','Pranav','Ankur','Prajwal','Nikita','Kabir']
# >>>Longest word : 'Prajwal' 

# In[ ]:


## your code ##


# Q. Create a function that replaces all the lowercase words with their uppercase versions and vice versa and centers the entire string in 100 spaces only if the 1st word of the string starts with a lowercase letter or ends with an exclamation mark.
# 
# 
# Note : There is no mistake in the output of string1 for words : Always to AlwAys ; upgradation to upgrAdAtion. Debug what might have caused it!
# 
# **Example **:
# 
# def string_modification(string):
#     ### your code here
# 
# string1 = "learning data science is too much fun! Always in a process of upgradation."
# 
# string_modification(string1)
# 
# >>> '            LEARNING DATA SCIENCE IS TOO MUCH FUN! AlwAys IN A PROCESS OF upgrAdAtion.             
# '
# 
# string2 = "Artificial Intelligence, BlockChain, Cybersecurity and Networking are going to mould the future!"
# 
# string_modification(string2)
# 
# >>> '  Artificial Intelligence, BlockChain, Cybersecurity AND Networking ARE GOING TO MOULD THE FUTURE!  '

# In[ ]:


## your code ##


# ### Difficulty Level : Hard

# Q. Create a function to sort the word in a sentence in an alphabetic order.
# 
# **Example :**
# 
# def order(sentence):
#        ### your code
# 
# order(sentence)
# 
# sentence = "The quick brown fox jumps over the lazy dog"
# >>> brown dog fox jumps lazy over quick The the
# 

# In[ ]:


## your code ##


# Q. Create a function that decodes a message encoded in Morse Code, displays the decoded message and the number of vowels and consonants present.
# 
# **Note** : Use String methods. Sharing a dictionary to help decode the message.
# 
# **Note** : Google about Morse Code for more information.
# 
# **Note** : '/' in the message specifies the space between words. ' ' between codes specifies the individual letters.
# 
# **Example :**
# 
# def decode_count(message):
#     ### your code here
# 
# 
# morse_code_dict = { 'A' : '.-', 'B' : '-...',
#                     'C' : '-.-.', 'D' : '-..', 'E' : '.',
#                     'F' : '..-.', 'G' : '--.', 'H' : '....',
#                     'I' : '..', 'J' : '.---', 'K' : '-.-',
#                     'L' : '.-..', 'M' : '--', 'N' : '-.',
#                     'O' : '---', 'P' : '.--.', 'Q' : '--.-',
#                     'R' : '.-.', 'S' : '...', 'T' : '-',
#                     'U' : '..-', 'V' : '...-', 'W' : '.--',
#                     'X' : '-..-', 'Y' : '-.--', 'Z' : '--..',
#                     '1' : '.----', '2' : '..---', '3' : '...--',
#                     '4' : '....-', '5' : '.....', '6' : '-....',
#                     '7' : '--...', '8' : '---..', '9' : '----.',
#                     '0' : '-----', ',' : '--..--', '.' : '.-.-.-',
#                     '?' : '..--..', '!' : '-.-.--','/' : '-..-.', 
#                     '-' : '-....-','(' : '-.--.', ')' : '-.--.-',}
# 
# message = '-.-. --- -. ... .. ... - . -. -.-. -.-- / .. ... / -.- . -.-- -.-.--'
# 
# decode_count(message)
# 
# >>> 
# Decoded Message :  CONSISTENCY IS KEY! 
# Number of Vowels :  5
# Number of Consonants :  15
# 

# In[ ]:


# morse_code_dict = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '!':'-.-.--','/':'-..-.', 
#                     '-':'-....-','(':'-.--.', ')':'-.--.-',}

# message = '-.-. --- -. ... .. ... - . -. -.-. -.-- / .. ... / -.- . -.-- -.-.--'



## your code ##

