text=input("enter the word")
text=text.lower();
text=text.replace("","");
rev=text[::-1]
if rev==text:
    print(rev)
    print("valid palindrome")
else:
    print(rev)
    print("invalid palindrome")