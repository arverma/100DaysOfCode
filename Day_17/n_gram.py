def text_mining(textstring,n):
    w = textstring.split()
    res = []
    # print(w, len(w))
    
    for i in range(len(w)-n+1):
        res.append(w[i:i+n])
    return res

print(text_mining("this is a capegemini. data science mcq", 3))