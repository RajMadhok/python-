balance=20000
operation=int(input("Press 1 for Credit and 2 for Debit: "))
print("ur balance is:",balance)
trans_amount=int(input("Enter the Amount:"))

i=1
while i<=3:
  if operation==1:
    credit=balance+trans_amount
    print("Your Current balance is: ",credit)
    print("Amount Credited: ",trans_amount)
    break;
  elif operation==2:
    if trans_amount>balance:
      print("Not enough balance.")
      break;
    elif  (trans_amount<=balance):
      debit=balance-trans_amount
      print("your current balance is: ",debit)
      print("Amount Debited: ",trans_amount)
      break;
  i=i+1
        
