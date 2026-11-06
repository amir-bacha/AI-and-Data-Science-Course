# Mobile Phone accesseries
# To find the expansive product 
# To find the cheapest product 

mobileAccessaries={} # An empty dictionary to which the items will be added

noOfAccessaries=int(input('How many accessaries do you want to add : '))

for x in range(noOfAccessaries):
    product=input(' Enter Accessaryv name : ')
    price=int(input('Enter the price of that Accessary : '))
    mobileAccessaries[product]=price

lowestPrice=float('inf')
cheapestAccessary=""
highestPrice=0
expansiveAccessary=''
betweenPrice=0
betweenItem=''
# To find the cheapest product
for item,price in mobileAccessaries.items():
    if(price<lowestPrice):
        lowestPrice=price
        cheapestAccessary=item

# To find the Expansive product
for item,price in mobileAccessaries.items():
    if(price>highestPrice):
        highestPrice=price
        expansiveAccessary=item

# To find the product of price between 350 and 500
for item,price in mobileAccessaries.items():
    if(price>=350 and price <=500):
        betweenPrice=price
        betweenItem=item
    else:
        betweenItem='No item of price between 350 t0 500'


print('The Cheapest Accessary is  ',cheapestAccessary," of its ",lowestPrice," lowest price")
print('The Expansive Accessary is ',expansiveAccessary," of its ",highestPrice," highest price")
print('item of price between 350 to 500 ',betweenItem, betweenPrice,)




