''' 
order of execution of decorators : 
- like recursive function. 
- but seems it is executing in revers order from the order of definition. 

'''    
def spliter_dec(func):
    print("spliter decorator construction starts")
    def spliter():
        print("spliter starts")
        str2 = func() 
        print("spliter ends")
        return str2.split()
    print("spliter decorator construction ends ")
    return spliter
    
def upper_dec(func):
    print ("upper decorator construction starts")
    def upper ():
        print("upper starts")
        str1 = func()  
        print("upper ends")
        return str1.upper()
    print( "upper decorator construction ends ")
    return upper
    
print ("Execution starts")

@spliter_dec 
@upper_dec
def ordinary():
    print ("Actual function ")
    return "good morning"

print(ordinary())
