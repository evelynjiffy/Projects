x= float(input("What is the buying cost?"))
y= float(input("What is the selling cost?"))

if y>x:
    print("profit")
    profit= y-x
    print(profit)
elif y==x:
    print("no profit, no loss")

else:
    loss= x-y
    print("loss", loss)
