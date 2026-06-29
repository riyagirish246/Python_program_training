def addTwoString(num1,num2):
    i=len(num)-1
    j=len(num)-1
    carry=0
    result=[]
    while i>=0 or j>=0 or carry:
        digit1=ord(num1[i])-ord(['0']) if i>=0 else 0
        digits2=ord(num2[j])-ord('0') if j>=0 else 0
        total =digit1+digit2+carry
        result.append(str(total1%10))
        carry=total//10
        i=1
        j=1
        return ''.join(result[::-1])
    

#main
num1=input("Enter the first Value:")
num1=input("Enter the second Value:")
print(addTwoString(num1,num2))