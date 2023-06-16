#Given 2 int values, return True if one is negative 
#and one is positive. Except if the parameter 
#"negative" is True, then return True 
#only if both are negative.

def pos_neg(a, b, negative):
  return (not negative and ((a < 0) != (b < 0))) or (negative and (a < 0 and b < 0))

pos_neg(1, -1, False) #→ True
pos_neg(-1, 1, False) #→ True
pos_neg(-4, -5, True) #→ True
