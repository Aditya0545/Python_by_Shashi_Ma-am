
def upper_lower():
    character = str(input("Enter Your String: "))
    uppers = 0
    lowers = 0
    for i in character:
        if i.isupper():
            uppers +=1
        elif i.islower():
            lowers +=1
        else:
            pass
    print(f"Lower Case : {lowers}\nUpper Case : {uppers}")    
    

upper_lower()
