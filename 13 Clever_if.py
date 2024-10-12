#clever if
#<var>=(false_val,true_val)[condition]
age=int(input("age:"))
vote=("no","yes")[age>=18]
print(vote)

sal=int(input("sal:"))
tax=sal*(0.1,0.2)[sal>10000]
print(tax)