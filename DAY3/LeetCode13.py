#Roman To Integer
inputRoman=input("Enter the roman value")
romanDict={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }
total=0
for i in range(len(inputRoman)-1):
    if romanDict[inputRoman[i]]<romanDict[inputRoman[i+1]]:
        total=total-romanDict[inputRoman[i]]
    else:
        total=total-romanDict[inputRoman[i]]

total=total+romanDict[inputRoman[-1]]
print(total)




