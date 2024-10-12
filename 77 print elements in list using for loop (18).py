#writing to a file
f=open("sem.text","w")#over writes the entire file
data=f.write("I am stronger")
print(data)
f1=open("sem.text","a")
d=f.write("I am confident")
print(d)
#python can read and write simultaneoulsy
#if there are no files , python can create a new file by itself automatically