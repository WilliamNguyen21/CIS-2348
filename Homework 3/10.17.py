#William Nguyen
#PSID: 1824617


class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str( self.item_price * self.item_quantity))

if __name__ == "__main__":
    print("Item 1")
    i1 = ItemToPurchase()
    i2 = ItemToPurchase()

    i1.item_name=input("Enter the item name:\n")
    i1.item_price= int(input("Enter the item price:\n"))
    i1.item_quantity = int(input("Enter the item quantity:\n"))
    print()
    
    print("Item 2")
    i2.item_name=input("Enter the item name:\n")
    i2.item_price= int(input("Enter the item price:\n"))
    i2.item_quantity = int(input("Enter the item quantity:\n"))
    print()

    print("TOTAL COST")
    i1.print_item_cost()
    i2.print_item_cost()
    print()
    total = (i1.item_quantity*i1.item_price + i2.item_quantity*i2.item_price)
    print("Total: $" + str(total))
    
          
