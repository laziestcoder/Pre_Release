print("*********Part 1: Auction Setup*********")

i_number =[]
i_des=[]
i_rprice=[]
i_bids=[0 for i in range(3)]
i_highbid=[0 for i in range (3)]
for i in range (0,3):
    num = int(input("Enter unique item number:"))
    while num in i_number:
        num=int(input("Item number already exist.Enter unique item number: "))
    i_number.append(num)
    des=input("Enter Description: ")
    i_des.append(des)
    price=float(input("Enter item's Reserved price: "))
    i_rprice.append(price)
