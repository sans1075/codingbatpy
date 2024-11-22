# Given two int values, return their sum. Unless the two values are the same, then return
# double their sum.

def sum_double(a, b):
  if a == b: return 4*a # Checks if a is equal to b, if so, returns four times a, because a + b would just equal 2 a
  return a+b # If the previous value is not returned, return the sum of a and b
