n=int(input("Enter the number:"))
def check(n):
    if(n%2==0):
        return("EVEN")
    else:
        return("ODD")
print(check(n))