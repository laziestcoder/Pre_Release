print("********** Task 1 Auction Setup *********")
item_number = []
item_name = []
item_description = []
item_reservedPrice = []
item_bids = []
item_numberOfBidsCount = []
item = int(input("How many items to be sold: "))
while item <10:
    item = int(input("Minimum 10 items. How many items to be sold: "))
item_bids = [0 for i in range(0,item)]
item_numberOfBidsCount = [0 for i in range(0,item)]
for i in range(0,item):
    number = int(input("Enter unique item number: "))
    while number in item_number:
        number = int(input("Item number already exist. Enter unique item number: "))
    item_number.append(number)
    name = input("Enter item name: ")
    item_name.append(name)
    description = input("Enter item description: ")
    item_description.append(description)
    reservedPrice = float(input("Enter item reserved price: "))
    item_reservedPrice.append(reservedPrice)



print("********** Task 2 Buyer Bids *********")
number = int(input("Enter item no. (Press -1 to Stop): "))
while number != -1:
    position = -1
    for i in range (0,item):
        if number == item_number[i]:
            position = i
            print("Item name is: ",item_name[position])
            print("Item description is: ",item_description[position])
            print("Item current highest bid: ",item_bids[position])
            buyerBid = input("Do you want to bid? (y/n) : ")
            if(buyerBid=="y" or buyerBid=="Y" ):
                buyerID = int(input("Enter Buyer Id: "))
                bid_amount = float(input("Enter your bid: "))
                if(bid_amount>item_bids[position]):
                    item_bids[position] = bid_amount
                    item_numberOfBidsCount[position]=item_numberOfBidsCount[position]+1  
    if(position == -1):
        print("No Item Found!")
    number = int(input("Enter item no. (Press -1 to Stop): "))
    



print("********* Task 3 At the End of the Auction **********")
total_amount = 0
total_sold = 0
total_unsold = 0
total_noBid = 0
sold = []
unsold = []
noBid = []
for i in range (0,item):
    if (item_numberOfBidsCount[i]>0):
        if(item_bids[i]>item_reservedPrice[i]):
            sold.append(item_number[i])
            total_amount = total_amount + item_bids[i]
            total_sold = total_sold + 1
        else:
            unsold.append(item_number[i])
            total_unsold = total_unsold + 1
    else:
        noBid.append(item_number[i])
        total_noBid = total_noBid + 1
print("Total Cost: ",(total_amount+total_amount*0.1))
print("Number of Sold Item: ",(total_sold))
print("Number of Unsold Item: ",(total_unsold))
print("Number of Nobid Item: ",(total_noBid))
print("Sold Items: ",(sold))
print("Unsold Items: ",(unsold))
print("Items with no bid: ",(noBid))
