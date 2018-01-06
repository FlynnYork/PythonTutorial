#Build with Python 2.7.14

def addToInventory(inventory, addedItems):
	for i in dragonLoot:
		#print i 
		inv.setdefault(i,0)       #add new value to inv dictionary, if there is not exist.
		#print inv[i]				 
		inv[i]+=1                 #count number
	#print inv
	return inv

def displayInventory(inventory):
	print 'Inventory was updated.'
	item_total = 0
	for j,k in inventory.items():		
		print str(k),j
		item_total = item_total + k
	print '\nTotal items number is '+str(item_total)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

newInv = addToInventory(inv, dragonLoot)
displayInventory(newInv)

