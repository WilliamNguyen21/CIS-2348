#William Nguyen
#PSID: 1824617

import datetime
class InventoryReports:

	# This is the Construtor
	def __init__(self, manufactureFile, priceFile, serviceFile):
		self.manufactureList = []
		self.priceDict = dict()
		self.serviceDateDict = dict()
		self.Data(manufactureFile, priceFile, serviceFile)
		self.Reports()
        # ServiceData method will put the service detials into the service dictionary
	def ServiceData(self, serviceFile):
		file = open(serviceFile)
		data = file.readlines()
		for line in data:
			split = line.strip().split(',')
			split[0] = int(split[0])
			self.serviceDateDict[split[0]] = split[1]
		file.close()

	# ManufactureData method will put the manufacturing details into the self.manufactureList
	def ManufactureData(self, manufactureFile):
		file = open(manufactureFile)
		d = file.readlines()
		for l in d:
			split = l.strip().split(',')
			split[0] = int(split[0])
			self.manufactureList.append(split)
		file.close()

	# PriceData method will load the price detials into self.priceDict
	def PriceData(self, priceFile):
		file = open(priceFile)
		d = file.readlines()
		for line in d:

			split = line.strip().split(',')
			for i in range(len(split)):
				split[i] = int(split[i])
			self.priceDict[split[0]] = split[1]
		file.close()

	# Data calls the other loading functions
	def Data(self, manufactureFile, priceFile, serviceFile):
		self.ManufactureData(manufactureFile)
		self.PriceData(priceFile)
		self.ServiceData(serviceFile)

	# TypeInventory will generate the csv files based on type of items.
	def TypeInventory(self):
		types = set()
		for x in self.fullInventory:
			types.add(x[2])
		for Name in types:
			filtered = []
			for x in self.fullInventory:
				if (x[2] == Name):
					copy = x[:]
					del copy[2]
					filtered.append(copy)
			Name = Name.capitalize()
			with open(Name + "Inventory.csv", 'w') as f:
				for x in sorted(filtered, key=lambda l:l[0]):
					f.write(','.join(map(str,x)) + "\n")


	# PastServiceInventory will generate the 'PastServiceDateInventory.csv'
	def PastServiceInventory(self):
		current = datetime.datetime.today()	
		filtered = [] 
		for x in self.fullInventory:
			CheckDate = datetime.datetime.strptime(x[-2], "%m/%d/%Y")
			if (CheckDate < current): 
				filtered.append(x)
		with open('PastServiceDateInventory.csv', 'w') as f:
			for x in sorted(filtered, key=lambda l:l[-2]):
				f.write(','.join(map(str,x)) + "\n")

	# FullInventory will generate the FullInventory.csv file
	def FullInventory(self):
		self.fullInventory = []
		for x in sorted(self.manufactureList, key=lambda l:(l[1], l[2])):
			current = x[:-1]
			current.append(self.priceDict[current[0]])
			current.append(self.serviceDateDict[current[0]])
			current.append(x[-1])
			self.fullInventory.append(current)
		with open('FullInventory.csv', 'w') as file:
			for x in self.fullInventory:
				file.write(','.join(map(str,x)) + "\n")

	# Damaged Inventory will genrate the "DamagedInventory.csv"
	def DamagedInventory(self):

		filtered = [] 
		for x in self.fullInventory:
			if (x[-1] == "damaged"):
				filtered.append(x[:-1])
		with open('DamagedInventory.csv', 'w') as f:
			for x in sorted(filtered, key=lambda l:l[3]):
				f.write(','.join(map(str,x)) + "\n")


	# Reports will call the other inventory functions
	def Reports(self):
		self.FullInventory()
		self.TypeInventory()
		self.PastServiceInventory()
		self.DamagedInventory()


	# the Query will ask the user for interactive queries
	def Query(self):
		noStop = True
		current = datetime.datetime.today()
		while noStop:
			Input = input("Enter manufacturer and item type (q for exit): ")
			if (Input.lower() == 'q'):
				print("Exiting...")
				noStop = False
			else:
				split = Input.split()
				if len(split) < 2:
					print("Invalid input.")
				else:
					split = split[-2:]
					manufacturer, itemType = split[0], split[1]
					filtered = []
					filteredManufacturer = []
					for x in self.fullInventory:
						serviceDate = datetime.datetime.strptime(x[-2], "%m/%d/%Y")
						if (x[2].strip().lower() == itemType.strip().lower() 
							and x[-1] != 'damaged' and serviceDate > current):
							if (x[1].strip().lower() == manufacturer.lower()):
								filtered.append(x)
							else:
								filteredManufacturer.append(x)
					if len(filtered) == 0:
						print("No such item in inventory")
					else:
						filtered = sorted(filtered, key=lambda l:l[3], reverse=True)
						print("Your item is:")
						print("Item ID:",filtered[0][0])
						print("Manufacturer:",filtered[0][1])
						print("Item type:",filtered[0][2])
						print("Price:",filtered[0][3])
						current_min = -1
						if len(filteredManufacturer) != 0:
							for i in range(len(filteredManufacturer)):
								if (abs(filteredManufacturer[i][3] - filtered[0][3]) < current_min or current_min == -1):
									index = i
									current_min = abs(filteredManufacturer[i][3] - filtered[0][3])
							print("\nYou may also consider:")
							print("Your item is:")
							print("Item ID:",filteredManufacturer[index][0])
							print("Manufacturer:",filteredManufacturer[index][1])
							print("Item type:",filteredManufacturer[index][2])
							print("Price:",filteredManufacturer[index][3])
							
manufacture = 'ManufacturerList.csv'
price = "PriceList.csv"
service = "ServiceDatesList.csv"

objective = InventoryReports(manufacture, price, service)
objective.Query()
