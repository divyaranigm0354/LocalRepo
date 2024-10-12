#BREAK AND CONTINUE
#BREAK : the loop exits / terminates  regardless of the condition. Once a break statement is encountered, the control is transferred to the first statement after the loop.
"""i=1
while i<=5:
    print(i)
    i=i+1
    if i==3:
        break
   """
   #Continue: except that condition it will print all values , it skips the condition

p=0
while p<=5:
    p=p+1
    if p==2:
        continue
    print(p)
 