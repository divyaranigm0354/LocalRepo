list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=36
i=0
for i in list:
    if(i==x):
        print("Element found at i=",i)
        break
    i=i+1
else:
    print("element not found")
