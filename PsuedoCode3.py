N=float(input("Enter the total units consumed:"))
bill=0
if (N<=100 and N>0):
bill=N*1.50
elif N<=200:
bill=(N*100)+(N-100)*2.50
else:
bill=(100*1.50)+(100*2.50)+(N-200)*4.00
print(f"total electricity bill")