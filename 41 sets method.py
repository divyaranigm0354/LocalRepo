collection={1, 4,3,"sweet","hdgd"}
collection.add(78.9)

print(collection)
collection.remove(4)
print(collection)
collection.add((9,8,7)) # it can be added
print(collection)
#collection.add([5,6,2]) #gives error immutable data type
collection.pop() #it takes random value , if we pass any value it throws error ,it doesnot take any arguments
print(collection)
#collection.clear()
#print(len(collection))

#UNION AND INTERSECTION
collection2={"avnish","ambika",22,21,1,3}
print(collection.union(collection2))
print(collection.intersection(collection2))
