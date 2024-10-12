with open ("demo.txt","r") as f:
     data=f.read()
     print(data)
with open("demo.txt","w")as f:
     data=f.write("my new data")
     print(data)