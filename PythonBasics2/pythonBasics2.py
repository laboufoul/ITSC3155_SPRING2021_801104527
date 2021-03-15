# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes a string of integers and
# counts how often each int appears within the string. returns the integer that appears
# the most amount of times

def count_threes(n):
  numbers = {}
  max_num_value = 0
  most_common = 0
  for i in n:
      if i not in numbers:
          numbers[i] = 1
      else:
        numbers[i] = numbers[i] + 1
  max_num_value = max(numbers.values())
  for x in numbers.keys():
      if numbers[x] == max_num_value:
          most_common = x
  most_common = int (most_common)
  return most_common







# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and stores each character and how often it appears in a dictionary
# then returns the letters that have the longest consecutive repeats
def longest_consecutive_repeating_char(s):
  letters = {}
  count = 0
  for x in range(len(s)-1):
   if (s[x] == s[x+1]):
      count += 1
      letters[s[x]] = count
   else:
      letters[s[x]] = count
      count = 0


  newLetters = {}
  max_count = max(letters.values())
  for x in letters.keys():
   if letters[x] == max_count:
      newLetters[x] = letters[x]

  return newLetters.keys()




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
