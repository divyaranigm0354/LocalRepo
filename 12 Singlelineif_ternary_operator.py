#Single line if / ternary operator

# Syntax <val>=<val1>if(condition)else<val2>

food=input("food:")
eat="yes" if food=="cake"else"no"
print(eat)

food1=input("food1:")
print("sweet")if(food=="cake" or "jalebi")else("not sweet")