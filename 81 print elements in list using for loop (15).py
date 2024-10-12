with open ("practice.text","w")as f:
    f.write("Hi everyone and I am divya\nI have pursued my graduation from UVCE College\n")
    f.write("I have an internship experience at cleartrip -flipkart group\nI worked in Hotel-Supply team and i have worked on a project called gen-ai based content relevance where I evaluated the hotel description to enhance the user experience ")

#write all occurence of have with had in the above file
with open ("practice.text","r")as f:    
    data=f.read()
    print(data)

    data.replace("i","me")
    print(data)

