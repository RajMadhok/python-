nterm=int(input("enter a number"))
n1=0
n2=1
count=0
if nterm<=0:
    print("pls enter a positive number")
elif nterm==1:
    print("fibonacci sequence upto ",nterm,":")
    print(n1)
else:
    print("fibonacci sequence upto",nterm,":")
    while count<nterm:
        print(n1,end=' , ')
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
