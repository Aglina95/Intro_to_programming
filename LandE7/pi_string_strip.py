# Write your code here :-)
filename = 'pi_30_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
#output:3.141592653589793238462643383279
#32
