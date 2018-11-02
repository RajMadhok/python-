bkname=input("enter name")
bkprice=int(input("enter bookprice"))
bkcode=int(input("enter bookcode"))
if (bkname=="python programming") and (bkprice>800):
           sm=bkprice*20/100
           print("sum is",sm)
           total=bkprice-sm
           print(total)
elif(bkname=="linux  shell script") and (bkprice>500) and (bkprice<800):
           sm1=bkprice*15/100
           print("sum is",sm1)
           total=bkprice-sm1
           print(total)
elif(bkprice<500):
     sm2=bkprice*10/100
     print("sum is",sm2)
     total=bkprice-sm2
     print(total)
else:
     sm3=bkprice*5/100
     print("sum is",sm3)
     total=bkprice-sm3
     print(total)
           
