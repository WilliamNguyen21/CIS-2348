#William Nguyen
#PSID: 1824617

import csv
from datetime import datetime

class inventory:

    def __init__(self, itemlist):
        self.itemlist = itemlist
        
    def fullinventory(self):
        with open('FullInventory.csv', 'w') as file:
            items = self.itemlist
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                manufacturername = items[item]['manufacturer']
                itemtype = items[item]['item_type']
                price = items[item]['price']
                servicedate = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,manufacturername,itemtype,price,servicedate,damaged))

#fullinventory() method will create a new csv file that will sort all of the inventory alphabetically by manufacturer

    def type(self):

        items = self.itemlist
        types = []
        keys = sorted(items.keys())
        for x in items:
            itemtype = items[x]['item_type']
            if itemtype not in types:
                types.append(itemtype)
        for type in types:
            filename = type.capitalize() + 'Inventory.csv'
            with open(filename, 'w') as file:
                for x in keys:
                    id = x
                    manfacturername = items[x]['manufacturer']
                    price = items[x]['price']
                    servicedate = items[x]['service_date']
                    damaged = items[x]['damaged']
                    itemtype = items[x]['item_type']
                    if type == itemtype:
                        file.write('{},{},{},{},{}\n'.format(id, manfacturername, price, servicedate, damaged))

#type() method will create a new csv files that are seperated by type
                        
    def service(self):
        items = self.itemlist
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse=True)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for x in keys:
                id = x
                manufacturername = items[x]['manufacturer']
                itemtype = items[x]['item_type']
                price = items[x]['price']
                servicedate = items[x]['service_date']
                damaged = items[x]['damaged']
                today = datetime.now().date()
                serviceexpire = datetime.strptime(servicedate, "%m/%d/%Y").date()
                expired = serviceexpire < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacturername, itemtype, price, servicedate, damaged))

#service() method will create a new csv file for items that are past their service date

    def damaged(self):
        items = self.itemlist
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory.csv', 'w') as file:
            for x in keys:
                id = x
                manufacturername = items[x]['manufacturer']
                itemtype = items[x]['item_type']
                price = items[x]['price']
                servicedate = items[x]['service_date']
                damaged = items[x]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, manufacturername, itemtype, price, servicedate))

#damged() method will create a new csv file for items that are damaged                     
                    
if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item = line[0]
                if file == files[0]:
                    items[item] = {}
                    manufacturername = line[1]
                    itemtype = line[2]
                    damaged = line[3]
                    items[item]['manufacturer'] = manufacturername.strip()
                    items[item]['item_type'] = itemtype.strip()
                    items[item]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item]['price'] = price
                elif file == files[2]:
                    servicedate = line[1]
                    items[item]['service_date'] = servicedate

#the following will call the methods and create the output files
    inven = inventory(items)
    inven.fullinventory()
    inven.type()
    inven.service()
    inven.damaged()
