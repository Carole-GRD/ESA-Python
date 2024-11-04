
# Algèbre de bool (silde 7)

# XOR
a = 2
b = 5
print('a = ', a, ' b = ',b)   # a =  2  b =  5

a = a ^ b
# 2 (en binaire : 010) XOR 5 (en binaire : 101) = 7 (en binaire : 111)
print('a = ', a, ' b = ',b)   # a =  7  b =  5

b = a ^ b
# 7 (en binaire : 111) XOR 5 (en binaire : 101) = 2 (en binaire : 010)
print('a = ', a, ' b = ',b)   # a =  7  b =  2

a = a ^ b
# 7 (en binaire : 111) XOR 2 (en binaire : 010) = 5 (en binaire : 101)
print('a = ', a, ' b = ',b)   # a =  5  b =  2