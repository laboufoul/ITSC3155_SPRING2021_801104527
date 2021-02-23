# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  counter = 0
  for i in range (0, n+1):
   if (i%3 == 0):
    if (i > 0):
     counter += 1
  return counter


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  most_common = s[0]
  for i in range (0, len(s)):
      for x in range (0, len(s)):
        if not (s[i] == s[x]):
          s.count(s[i:x])
        if s.count(s[i:x]) > s.count(s[i+1:x+2]):
            most_common = s[i]
  return most_common


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  for i in range (0, len(s)):
      if s[i].lower() == s[-(i+1)].lower():
       return True
      else:
       return False
