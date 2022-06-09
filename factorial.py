
def myfunc(n):
   if n == 1:
       return n
   else:
       return n*myfunc(n-1)
num=int(input("Enter number to find factorial:"))
if num < 0:
   print("factorial does not exist ")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print('The factorial of number is' ,myfunc(num))
