# Given 3 int values, a b c, return their sum. However, if one of the values is the same as
# another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  if c == a == b: return 0 # Returns 0 if they are all the same
  if a == b: return c # Returns c if a and b are the same
  if b == c: return a # Returns a if b and c are the same
  if c == a: return b # Returns b if a and c are the same
  return a + b + c # Returns the sum if they are all different
