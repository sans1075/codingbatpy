# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is
# True, in which case return True if the number is less or equal to 1, or greater or equal to
# 10.

def in1to10(n, outside_mode):
  return (not outside_mode and n <= 10 and n >= 1) or (outside_mode and (n >= 10 or n <= 1)) # Returns True if conditions are met
