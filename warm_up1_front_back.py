# Given a string, return a new string 
# where the first and last chars have 
# been exchanged.

def front_back(str):
  return str if len(str) <= 1 else str[::-1] if len(str) == 2 else str[len(str) - 1] + str[1:len(str) - 1] + str[0]

print(front_back('code')) #→ 'eodc'
print(front_back('a')) #→ 'a'
print(front_back('ab')) #→ 'ba'
