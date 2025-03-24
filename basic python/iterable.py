a=0
password = 123
while a<3 :
  try:
    number= int(input("pls enter ATm pin : "))
    if number == password :
      print ("Amount debited")
      else:
        print("No debit")
        a=a+1
        except:
          print