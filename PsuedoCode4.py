n=int(input("Enter a number"))
square=n*n
digits=len(str(n))
left = square//(10**digits)
right= square%(10**digits)
if (left+right==n):
    print("Keprekar Number")
else:
    print("Not Keprekar Number")