# bug / exceptions
# 신기하다 똑똑한 python

def divide (a,b):
    try :
        return a/b
    except ZeroDivisionError:
        return "nope"

print(divide(4,2))
print(divide(4,0))



class IHateAError(Exception):
    pass

def getinput():
    b=input()
    if b == "a" or b=="A":
        raise IHateAError # A or a cause an Error!
    else:
        return print(b)

getinput()
