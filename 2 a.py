    def f(n):
    if n==1 or n==0:
        return 1
    return (f(n-1)+f(n-2))

n=int(input("enter n"))
if n<=0:
            print("enter n>0")
            exit
for i in range (n):
            print(f(i))
