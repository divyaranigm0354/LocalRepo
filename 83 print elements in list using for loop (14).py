with open ("practice.text","r")as f:    
    data=f.read()
    print(data)

new_data=data.replace("have","had")
print(new_data)

