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
		f = open(serviceFile)
		data = f.readlines()
		for line in data:
			splitted = line.strip().split(',')
			splitted[0] = int(splitted[0])
			self.serviceDateDict[splitted[0]] = splitted[1]
		f.close()

	# ManufactureData method will put the manufacturing details into the self.manufactureList
	def ManufactureData(self, manufactureFile):
		f = open(manufactureFile)
		data = f.readlines()
		for line in data:
			splitted = line.strip().split(',')
			splitted[0] = int(splitted[0])
			self.manufactureList.append(splitted)
		f.close()

	# PriceData method will load the price detials into self.priceDict
	def PriceData(self, priceFile):
		f = open(priceFile)
		data = f.readlines()
		for line in data:

			splitted = line.strip().split(',')
			for i in range(len(splitted)):
				splitted[i] = int(splitted[i])
			self.priceDict[splitted[0]] = splitted[1]
		f.close()

	# Data calls the other loading functions
	def Data(self, manufactureFile, priceFile, serviceFile):
		self.ManufactureData(manufactureFile)
		self.PriceData(priceFile)
		self.ServiceData(serviceFile)

	# TypeInventory will generate the csv files based on type of items.
	def TypeInventory(self):
		types = set()
		for entry in self.fullInventory:
			types.add(entry[2])
		for typeName in types:
			filteredEntries = []
			for entry in self.fullInventory:
				if (entry[2] == typeName):
					copyList = entry[:]
					del copyList[2]
					filteredEntries.append(copyList)
			typeName = typeName.capitalize()
			with open(typeName + "Inventory.csv", 'w') as f:
				for entry in sorted(filteredEntries, key=lambda l:l[0]):
					f.write(','.join(map(str,entry)) + "\n")


	# PastServiceInventory will generate the 'PastServiceDateInventory.csv'
	def PastServiceInventory(self):
		currentDate = datetime.datetime.today()	
		filteredEntries = [] 
		for entry in self.fullInventory:
			dateToCheck = datetime.datetime.strptime(entry[-2], "%m/%d/%Y")
			if (dateToCheck < currentDate): 
				filteredEntries.append(entry)
		with open('PastServiceDateInventory.csv', 'w') as f:
			for entry in sorted(filteredEntries, key=lambda l:l[-2]):
				f.write(','.join(map(str,entry)) + "\n")

	# FullInventory will generate the FullInventory.csv file
	def FullInventory(self):
		self.fullInventory = []
		for entry in sorted(self.manufactureList, key=lambda l:(l[1], l[2])):
			currentList = entry[:-1]
			currentList.append(self.priceDict[currentList[0]])
			currentList.append(self.serviceDateDict[currentList[0]])
			currentList.append(entry[-1])
			self.fullInventory.append(currentList)
		with open('FullInventory.csv', 'w') as f:
			for entry in self.fullInventory:
				f.write(','.join(map(str,entry)) + "\n")

	# Damaged Inventory will genrate the "DamagedInventory.csv"
	def DamagedInventory(self):

		filteredEntries = [] 
		for entry in self.fullInventory:
			if (entry[-1] == "damaged"):
				filteredEntries.append(entry[:-1])
		with open('DamagedInventory.csv', 'w') as f:
			for entry in sorted(filteredEntries, key=lambda l:l[3]):
				f.write(','.join(map(str,entry)) + "\n")


	# Reports will call the other inventory functions
	def Reports(self):
		self.FullInventory()
		self.TypeInventory()
		self.PastServiceInventory()
		self.DamagedInventory()


	# the Query will ask the user for interactive queries
	def Query(self):
		notQuit = True
		currentDate = datetime.datetime.today()
		while notQuit:
			userInput = input("Enter manufacturer and item type (q for exit): ")
			if (userInput.lower() == 'q'):
				print("Exited")
				notQuit = False
			else:
				splitted = userInput.split()
				if len(splitted) < 2:
					print("Invalid input.")
				else:
					splitted = splitted[-2:]
					manufacturer, itemType = splitted[0], splitted[1]
					filteredEntries = []
					filteredEntriesManufacturer = []
					for entry in self.fullInventory:
						serviceDate = datetime.datetime.strptime(entry[-2], "%m/%d/%Y")
						if (entry[2].strip().lower() == itemType.strip().lower() 
							and entry[-1] != 'damaged' and serviceDate > currentDate):
							if (entry[1].strip().lower() == manufacturer.lower()):
								filteredEntries.append(entry)
							else:
								filteredEntriesManufacturer.append(entry)
					if len(filteredEntries) == 0:
						print("No such item in inventory")
						filteredEntries = sorted(filteredEntries, key=lambda l:l[3], reverse=True)
						print("Your item is:")
						print("Item ID:",filteredEntries[0][0])
						print("Manufacturer:",filteredEntries[0][1])
						print("Item type:",filteredEntries[0][2])
						print("Price:",filteredEntries[0][3])
						current_min = -1
						if len(filteredEntriesManufacturer) != 0:
							for i in range(len(filteredEntriesManufacturer)):
								if (abs(filteredEntriesManufacturer[i][3] - filteredEntries[0][3]) < current_min or current_min == -1):
									index = i
									current_min = abs(filteredEntriesManufacturer[i][3] - filteredEntries[0][3])
							print("\nYou may also consider:")
							print("Your item is:")
							print("Item ID:",filteredEntriesManufacturer[index][0])
							print("Manufacturer:",filteredEntriesManufacturer[index][1])
							print("Item type:",filteredEntriesManufacturer[index][2])
							print("Price:",filteredEntriesManufacturer[index][3])





manufactureFile = 'ManufacturerList.csv'
priceFile = "PriceList.csv"
serviceFile = "ServiceDatesList.csv"

objective = InventoryReports(manufactureFile, priceFile, serviceFile)
objective.Query()
