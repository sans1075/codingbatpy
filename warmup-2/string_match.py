# Given 2 strings, a and b, return the number of the positions where they contain the same
# length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az"
# substrings appear in the same place in both strings.

def string_match(a, b):
  count = 0 # Initializes the count
  for i in range(len(a)-1): # Iterates through string a
    if a[i:i+2] == b[i:i+2]: count += 1 # Increments the count if the same length 2 substring is in the same position in each string
  return count # Returns the count
