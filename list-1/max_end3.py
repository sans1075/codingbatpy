# Given an array of ints length 3, figure out which is larger, the first or last element in the
# array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  return [max(nums[0], nums[2]), max(nums[0], nums[2]), max(nums[0], nums[2])] # Returns the larger of the two numbers 3 times
