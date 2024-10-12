#recursion is when a fuction calls itself repeatedly
def show(n):
    if(n==0):#BASE CASE (it decides the whther recursion should stop or not)
     return
    print(n)
    show(n-1)

show(5)