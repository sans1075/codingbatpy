# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  string = "" # Initializes an empty string
  for i in range(len(str)): # Repeats for the length of str
    string += str[:i+1] # Adds the characters from str to the empty string
  return string # Returns the new string
