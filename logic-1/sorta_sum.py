# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are
# forbidden, so in that case just return 20.

def sorta_sum(a, b):
  if a + b < 10 or a + b > 19: return a + b # Returns the sum if it is an allowed number
  return 20 # Returns 20 if the sum is a forbidden number
