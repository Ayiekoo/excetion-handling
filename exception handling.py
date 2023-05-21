#!/usr/bin/env python
# coding: utf-8

# In[1]:


### basic input and user intercation
name = input("Enter your name")
age = input("Enter your age: ")
print("Hello,", name)
print("You are", age, "years old")


# In[4]:


### we can convert inputs to data types
num1 = int(input("Enter a number: "))
num2 = float(input("Enter another number: "))
result = num1 + num2
print("The sum is:", result)


# In[6]:


### COMMENTS AND CODE DPCUMENTATION

## THIS US A SINGLE-LINE COMMENT
"""
This is a multi-line comment
Ypu can have multiple line comments to provide detailed explanation or document to your code
"""

def calculate_square(num):
    """
    This function will calculate teh square of a given number.
    :param num: The number to be squared.
    :return: The square of the number.
    """
    return num ** 2
result = calculate_square(4)
print(result)


# In[7]:


def calculate_square(num):
    return num ** 2
result = calculate_square(225)
print(result)


# In[9]:


## control flow ##

"""
conditional statements; if, elif, and else
break and continue statements
exception handling like try, except and finally
"""

# conditional statements; elif, if and else

x = 10

if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")


# In[15]:


total = raw_input('What is the total amount for your online shopping?')
country = raw_input('Shipping within the US or Canada?')

if country == "US":
    if total <= "50":
        print "Shipping Costs $6.00"
    elif total <= "100":
print(Shipping Costs $9.00)
    elif total <= "150":
            print "Shipping Costs $12.00"
    else:
        print(FREE)

if country == "Canada":
    if total <= "50":
        print "Shipping Costs $8.00"
    elif total <= "100":
        print "Shipping Costs $12.00"
    elif total <= "150":
        print "Shipping Costs $15.00"
    else:
        print(FREE)


# In[16]:


## BREAK AND CONTINUE STATEMENTS
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
    
for num in numbers:
    if num == 3:
        continue
    print(num)


# In[18]:


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 2:
        break
    print(num)


# In[19]:


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 4:
        break
    print(num)


# In[20]:


# Exception handling (try, except, finally)
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("An error occured:", str(e))
finally:
    print("Finally block")

class CustomerError(Exception):
    pass

try:
    raise CustomerError("This is a custom exception")
except CustomerError as ce:
    print("Custom Error:", str(ce))


# In[ ]:




