# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array
# somewhere.

def array123(nums):
  return "123" in "".join(str(num) for num in nums) # Returns true if 123 is in the array in that order
