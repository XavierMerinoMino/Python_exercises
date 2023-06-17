# Return the number of times that 
# the string "hi" appears anywhere 
# in the given string.

# Usign built-in function
# def count_hi(str):
#   return str.count('hi')

# Using the string as list
# def count_hi(str):
#   if 'hi' not in str:
#     return 0
#   else:
#     parts = str.split('hi')
#     return len(parts) - 1

# Using more traditional functions
def count_hi(str):
  count = 0
  found = False
  for c in str:
    if c == 'h':
      found = True
      continue

    if c == 'i' and found:
      count += 1
      found = False

  return count

print(count_hi('abc hi ho')) #→ 1
print(count_hi('ABChi hi')) #→ 2
print(count_hi('hihi')) #→ 2
print(count_hi('heha')) #→ 0
