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
  numbers = {} # declare empty dictionary
  max_num_value = 0 #declare variable to 0
  most_common = 0 #initialize most common multiple to be 0
  for i in n: #adding each individual number in string to dictionary
      if i not in numbers: #if key not in dictionary
          numbers[i] = 1#key has value of 1
      else:#if key in dictionary
        numbers[i] = numbers[i] + 1#key's value increases by 1 each time it appears
  max_num_value = max(numbers.values())#max number is the highest value in dictionary
  for x in numbers.keys():
      if numbers[x] == max_num_value:#finding most common number
          most_common = x#most common is equal to the key that corresponds to value max_num_value
  most_common = int (most_common)#type casting most common to an integer
  return most_common#return most common







# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and stores each character and how often it appears in a dictionary
# then returns the letters that have the longest consecutive repeats
def longest_consecutive_repeating_char(s):
  letters = {}#declare empty dictionary
  count = 0#initialize count to 0
  for x in range(len(s)-1):#for every char in string s
   if (s[x] == s[x+1]):#if two consecutive chars are the same
      count += 1#increase count
      letters[s[x]] = count#letters at value of char equals to its count
   else:#if two consecutive chars are not the same
      letters[s[x]] = count#value of letters at char equals to count
      count = 0#reset count to 0

  dict = {}#declare an empty dictionary
  max_count = max(letters.values())#max count is the highest value in letters
  for x in letters.keys():#for every key in letters
   if letters[x] == max_count:#if value in letters is equal to max_count
      dict[x] = letters[x]#value of dictionary at x is equal to value of letters at x

  return dict.keys()#return keys of dictionary




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

