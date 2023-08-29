num=int(input("enter the number"))
onum=num
rev=0
digits=list()
for i in range(10):
    digits.append(0)
while num>0:
    dig=(num%10)
    digits[dig]+=1
    rev=rev*10+(num%10)
    num=num//10
print(rev)
if onum==rev:
    print("palindrome")
else:
    print("not a palindrom")
print(digits)
