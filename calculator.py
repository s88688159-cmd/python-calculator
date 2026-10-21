num1 = float(input("Enter first number:") 
num2 = float(input("Enter second number:") 

print("choose:+,-,*,/") 
op = input("Enter operation:") 

if op =="+":
  print("answer":,num1 + num2) 
elif op == "-":
  print("answer":,num1 - num2) 
elif op =="*":
  print('answer":,num1*num2) 
elif op=="/": 
if num2 !=0:
  print("answer":,num1/num2) 
else:
   print("cannot divide by zero") 
else:
   print("invalid operation")
