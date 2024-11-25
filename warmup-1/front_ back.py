# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) > 1: return str[-1] + str[1:-1] + str[0] # Returns the string with the letters swapped if the length is greater than 1
  return str # If not, just return the string
