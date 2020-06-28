#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 3. To find unique element from a list
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,2,3,3,4,4,5])) 


# In[6]:


# 5. function that accepts a string and calculate the no.of upper & lower cases
def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1
            print (uppercase_letter_count, lowercase_letter_count)
count_upper_lower("Hello Mr. Rogers, how are you this fine Tuesday?")


# In[11]:


# 4. Function that checks whether a number is in a given range
def test_range(n):
    if n in range(2,10):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


# In[10]:


# 1. To print integers 1to 100.multiples of 3="Fizz", 5="Buzz", 3&5="FizzBuzz"
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    else:
        return num

for n in range(1,100):
    print(fizz_buzz(n))


# In[12]:


# 2. to remove consecutive duplicatives from a list
from itertools import groupby
def compress(l_nums):
    return [key for key, group in groupby(l_nums)] 
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
print("Original list:") 
print(n_list)
print("\nAfter removing consecutive duplicates:")
print(compress(n_list)) 


# In[ ]:




