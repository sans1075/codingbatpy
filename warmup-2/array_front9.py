# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The 
# array length may be less than 4.

def array_front9(nums):
  return 9 in nums[0:4] # Returns True if there is a 9 in the first 4 elements of the array
