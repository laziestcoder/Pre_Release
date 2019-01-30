#Task 1
item_number_list = list(range(1, 12))
item_name_list = ["phone", "postcard", "car", "pen", "tablet", "pencil case", "laptop", "mouse", "keyboard", "motherboard", "monitor"]
description_list = ["iPhone XS", "New Zealand City View", "BMW i8",
                    "Schneider Limited Edition", "iPad Pro 12.9in", "Kokuyo Limited",
                    "ASUS Zenbook Pro 15", "Magic Mouse", "Cherry MX. 8.0",
                    "MSI Brand", "Samsung Brand 21 inch"]
reserve_price_list = [300, 15, 50000, 100, 2027, 50, 1099, 129, 699, 1000000000, 6000, 00]
bid_number_list = [0]*11




# Task 2

highest_bid_price_list = [0]*11
buyer_number_list = ["1", "2", "3", "4", "5", "6"]
number_of_bid = [0]*11
sold = [False]*11
# used in task 3
item_highest_bid_holder_list = [""]*11
total_auction_fee = 0
total_sold_item = 0
total_money = 0



# Print all item and item number
while True:
    for i in range(len(item_name_list)):
        item_number_current = str(item_number_list[i])
        current_item_name = str(item_name_list[i])
        print(item_number_current + ": " + current_item_name)

    restart = False
    exit_loop = False
    name_search = input("Please enter the item name or write 'display_list': ")
    name_search = name_search.casefold()
    if name_search == "display_list":
        displayInfo()
    elif name_search not in item_name_list:
        print("Invalid input. Item not found. Try again!\n")
        continue
    else:
        search_index = item_name_list.index(name_search)
        current_description = description_list[search_index]
        current_bid_count = number_of_bid[search_index]
        sold_status = sold[search_index]
        item_highest_bid = float(highest_bid_price_list[search_index])
        item_highest_bid_with_dollar_sign = "$" + str(item_highest_bid)
        print("Description: " + current_description)
        print("Current highest bid is " + item_highest_bid_with_dollar_sign)
        print("Number of Bids: %d" % current_bid_count)
        if sold_status:
            print("Sold: Yes")
        else:
            print("Sold: No")
        if sold_status != True:
            purchase_status = input("\nDo you want to purchase? Y/N: ")
            purchase_status = purchase_status.casefold()

            while purchase_status == "y":
                buyer_number_check = str(input("Please enter your buyer number: "))
                while buyer_number_check in buyer_number_list:
                    print("\nIdentity verified.")
                    buyer_bid = float(input("Please enter your bid: "))
                    # no type check or type conversion is need because if it is not a number,
                    # then it will automatically fail the condition
                    if buyer_bid > item_highest_bid:
                        item_highest_bid = buyer_bid
                        highest_bid_price_list[search_index] = float(item_highest_bid)
                        bid_number_list[search_index] += 1
                        item_highest_bid_holder_list[search_index] = buyer_number_check
                        print("Congratulation! Your bid is the current highest.")
                        number_of_bid[search_index]+= 1;
                        print("\nYet you are free to give another higher bid.")
                        while True:
                            further_bid = input("Do you want to give another bid or allow others to bid? Y/N : ")
                            further_bid = further_bid.casefold()
                            if further_bid == "y":
                                restart = True
                                break
                            elif further_bid == "n":
                                exit_loop = True
                                break
                            else:
                                print("Sorry, error in input")
                                continue
                    else:
                        print("Your bid is lower than the current highest bid, please try again.\n")
                        continue
                    if restart:
                        break
                    elif exit_loop:
                        break
                else:
                    print("Identify verification failed. Please try again.")
                    continue
                if restart:
                    break
                elif exit_loop:
                    break
            else:
                print("Purchasing process canceled.\n")
                continue
            if restart:
                print()
                continue
            elif exit_loop:
                break

#task 3
#def displayInfo():
print("\n\n------------------------------------------------------------")
for i in range(1,11):
    if sold[i] != True and highest_bid_price_list[i] > reserve_price_list[i]:
        sold[i] = True
        total_sold_item += 1
        total_money += highest_bid_price_list[i]
        total_auction_fee += (highest_bid_price_list[i]*0.10)

#total money and total auction company fee
print("\n\nTotal Money: %d" % total_money)
print("Total Auction Company Fee: %d" % total_auction_fee)
print("Total Sold Items: %d " % total_sold_item)

#sold items
print("\n\nSold Items: ")
flag = True
soldItemsNumber = 0
for i in range (1,11):
    if sold[i] == True:
        flag = False
        soldItemsNumber += 1
        print("Item Name: %s " % item_name_list[i])
        print("Description: %s " % description_list[i])
        print("Number of Bids: %d "% number_of_bid[i])
        print("Sold Money: %d "% highest_bid_price_list[i])
if flag:
    print("No item sold.\n")
else:
    print("\nTotal %d Sold Items" % soldItemsNumber)


#unsold items
print("\n\nUnsold Items: ")
flag = True
notSoldItemsNumber = 0
for i in range (1,11):
    if sold[i] == False and number_of_bid[i] > 0:
        flag = False
        notSoldItemsNumber += 1
        print("Item Name: %s " % item_name_list[i])
        print("Description: %s " % description_list[i])
        print("Number of Bids: %d "% number_of_bid[i])
        print("Highest Bid: %d "% highest_bid_price_list[i])
if flag:
    print("No item found.\n")
else:
    print("\nTotal %d Unsold Items" % notSoldItemsNumber)


#not bid items
print("\n\nNot Bid Items: ")
flag = True
notBidItemsNumber = 0
for i in range (1,11):
    if sold[i] == False and number_of_bid[i] == 0:
        flag = False
        notBidItemsNumber += 1
        print("Item Name: %s " % item_name_list[i])
        print("Description: %s " % description_list[i])
        print("Number of Bids: %d "% number_of_bid[i])
        print("Reserve Money: %d "% highest_bid_price_list[i])
if flag:
    print("No item found.\n")
else:
    print("\nTotal %d Not Bid Items" % notBidItemsNumber)
