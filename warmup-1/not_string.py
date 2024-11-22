# Given a string, return a new string where "not " has been added to the front. However, if
# the string already begins with "not", return the string unchanged.

def not_string(str):
  if str[:3] == "not": return str # Returns string unchanged if it already starts with not
  return "not " + str # If the string doesn't start with not, returns the string with not appended to the front
