# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# import regular expression module
import re

# Part A. ends_with_consonant(s)
# Define a function ends_with_consonant(s) that takes a string and returns true
# if it ends with a consonant and false otherwise.
# (For our purposes, a consonant is any letter other than A, E, I, O, U.)
# Note: Be sure to use RegEx and it works for both upper and lower case and for nonletters!

def ends_with_consonant(s):
<<<<<<< HEAD
  regex = r"([AEIOUaeiou])"
  lastChar = s[len(s)]
  if (re.search(regex, lastChar)):
      return False
  return True
=======
  regex = r"[AEIOUYaeiouy]"
  lastChar = s[len(s)-1]
  if re.search(regex, lastChar):
    return True
  return False

>>>>>>> c8a676edf2a2672bc4a5aa56e58cea7dcb5185e9




 # Part B. ends_with_number
# Define a function ends _with_number(s) that takes a string and returns true
# if it ends with a number and false otherwise.
# (For our purposes, a number is any character that is 0,1,2,3,4,5,6,7,8, or 9.)
# Note: Be sure to use RegEx!
def ends_with_number(s):
  regex = r"(\d+)"
<<<<<<< HEAD
  lastChar = s[len(s)]
  if (re.search(regex, lastChar)):
      return True
=======
  lastChar = s[len(s)-1]
  if re.search(regex, lastChar):
    return True
>>>>>>> c8a676edf2a2672bc4a5aa56e58cea7dcb5185e9
  return False


# Part C. binary_multiple_of_6
# define a method binary_multiple_of_4(s) that takes a string and returns true
# if the string represents a binary number that is a multiple of 6.
# Note: Be sure it returns false if the string is not a valid binary number!
# Hint: Use regular expressions to match for the pattern of a binary number that is a multiple of 6.
def binary_multiple_of_6(s):
<<<<<<< HEAD
  return True
=======
  regex = r"10"
  lastTwoChars = s[len(s)-2:len(s)]
  if(re.search(regex, lastTwoChars)):
    return True
  return False
>>>>>>> c8a676edf2a2672bc4a5aa56e58cea7dcb5185e9
