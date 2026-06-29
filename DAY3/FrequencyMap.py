number=list(map(int,input("Enter the number:").split()))
k=int(input("Enter the threshold value: "))
freq=dict()
for num in number:
    freq[num]=freq.get(num,0)+1
for num,count in freq.items():
    if count>k:
        print(f"{num} : {count} times")
