# example of an while loop 
print ' conversion table from celcius to farenhite '
C = -20

dc = 5

while C <= 40:
   
    F = (9.0/5)*C +32
    print  C, F
    C = C+dc          #notice no end loop option. Lines inside the loop 
                      #must be start writing at column greater than' while ' 

print '......'
 

# example for how to do factorial ! 
# Lets find out Sin = x - (x^3 / 3!) + (x^5/5!) -(x^7/7!) + .... 

print ' value of sinx '
p = 1
sin = 0.0
x = 2.0
sign = 1
import math
while p<=5 :
     
    value = (sign*(x**p)) / math.factorial(p)
    sin = sin + value 
    sign = -sign 
    p =p+2 
print sin
