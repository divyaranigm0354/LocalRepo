#if-elif-else
salary=int(input("salary:"))
if(salary>10000):
  salary+=2000
elif(salary>20000):
  salary+=3000
else:
  salary+=1000
print(salary)

"""
Syntax is
if(condition):
  staement
  elif(condition):
  statement
  else
  statement"""