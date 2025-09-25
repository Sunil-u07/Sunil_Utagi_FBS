#Q7. Sum of 3 digits and digit separate output
num = int(input("Enter a number: "))
d1=num%10
num=num//10

d2=num%10
num=num//10
 
d3=num%10
num=num//10

print(f'd1:{d1}, d2:{d2}, d3:{d3}')

print(f'The sum of the 3 digits is: {d1+d2+d3}')