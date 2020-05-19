def say(message,times = 1):
    print(message * times)

say("Hello")
say("World", 5)

def func(a, b=5,c=5):
    print("x is",a,"and b is",b,"and c is",c)

func(3,7)
func(25, c=24)
func(c=50, a=100)

#FUNGSI RETURN

def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return "The Numbers are equal"
    else:
        return y

print(maximum(2,3))