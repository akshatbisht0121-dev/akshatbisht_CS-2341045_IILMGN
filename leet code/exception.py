a = 10
try:
    b= int(input("enter a number :"))
    c = a/b
except ValueError:
    print ("value error")
finally:
    print(c)    