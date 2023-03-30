toBuyList = ['apple', 'candies', 'watermelon']
print(toBuyList)

## add item
buyItem = input('Write a food you would like to buy at the grocery store: ')
toBuyList.append(buyItem)

print(toBuyList)

## place item
itemPlaceRealocated = int(input(f'Where would you like to place the {buyItem} you just added?: '))
toBuyList.pop(3)
toBuyList.extend(buyItem)
print(toBuyList)

## delete item
dontBuyItem = int(input('Write the food number you would like to delete from this grocery store list: '))
toBuyList.pop(dontBuyItem)
print(toBuyList)