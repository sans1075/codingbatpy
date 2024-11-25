# Given a string, return the count of the number of times that a substring length 2 appears
# in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't
# count the end substring).

def last2(str):
  count = 0 # Initializes the counter
  for i in range(len(str)): # Repeats for the length of the string
    if str[i:i+2] == str[-2:] and i not in [len(str)-1, len(str)-2] : count += 1 # If the character and next character equals the
    # end of the string, and it is not the end of the string, increment counter.
  return count # Returns the count
