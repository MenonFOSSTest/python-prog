s=input("enter the given character")
y=''.join(reversed(s))
if(s==y):
    print(s,":IT IS A PALINDROME")
else:
    print(s,":IT IS NOT A PALINDROME")
