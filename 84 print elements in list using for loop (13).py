with open("practice.text","r")as f:
    data=f.read()
    print(data)

if(data.find("experience")):
     print("YES")
else:
     print("NO")