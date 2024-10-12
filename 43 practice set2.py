"""sub1="maths"
marks=int(input("Enter the marks of sub1:"))
sub2="science"
marks=int(input("Enter the marks of sub2:"))
sub3="maths"
marks=int(input("Enter the marks of sub3:"))
dict={"sub1":"marks","sub2":"marks","sub3":"marks"}
print(dict) failed pgm"""


dict={}
print(dict)


marks1=int(input("Enter the marks of sub1:"))
dict.update({"phy":marks1})
marks2=int(input("Enter the marks of sub2:"))
dict.update({"chem":marks2})
marks3=int(input("Enter the marks of sub3:"))
dict.update({"bio":marks3})
print(dict)

