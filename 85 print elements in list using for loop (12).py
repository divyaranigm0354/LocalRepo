def check_line():
    word = "experience"
    data = True
    linecount = 1
    
    with open("practice.text", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(linecount)
                return
            linecount += 1  # This should be at the same level as the if block
    
    return -1

check_line()
