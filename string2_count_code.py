# Return the number of times that the string 
# "code" appears anywhere in the given string, 
# except we'll accept any letter for the 'd', 
# so "cope" and "cooe" count.

def count_code(str):
  cad = 'code'
  count = 0
  indx = 0
  for c in str:
    if c == cad[indx] or indx == 2:
      indx += 1

      if indx == 4:
        indx = 0
        count += 1
    else:
      if c == cad[0]:
        indx = 1
      else:
        indx = 0

  return count

count_code('AAcodeBBcoleCCccoreDD') #→ 3
print(count_code('cozfxxcope')) #→ 1
print(count_code('aaacodebbb')) #→ 1
print(count_code('codexxcode')) #→ 2
print(count_code('cozexxcope')) #→ 2
