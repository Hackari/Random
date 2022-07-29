import random
from tabulate import tabulate
a=0
minecraft = ["Stone Age","Getting an Upgrade","Acquire Hardware","Suit Up","Hot Stuff","Isn't It Iron Pick","Not Today, Thank You","Ice Bucket Challenge","Diamonds!","We Need to Go Deeper"]
nether = ["A Terrible Fortress","Return to Sender","Those Were the Days","Who is Cutting Onions?","Oh Shiny","This Boat has Legs","War Pigs"]
adventure = ["Monster Hunter","Sweet Dreams","Take Aim","What a Deal!","Hired Help","Bee Our Guest","Sticky Situation","Voluntary Exile","Ol'Betsy"]
husbandary = ["A Seedy Place","Best Friends Forever","The Parrots and the Bats"]

combinelist = []
combinelist.extend(minecraft)
combinelist.extend(nether)
combinelist.extend(adventure)
combinelist.extend(husbandary)
finalist1 = []
finalist2 = []
finalist3 = []
finalist4 = []
finalist5 = []
finalist = []
for i in range(5):
     x = len(combinelist)
     y = random.randint(0,x-1)
     finalist1.append(combinelist[y])
     del(combinelist[y])
for i in range(5):
     x = len(combinelist)
     y = random.randint(0,x-1)
     finalist2.append(combinelist[y])
     del(combinelist[y])
for i in range(5):
     x = len(combinelist)
     y = random.randint(0,x-1)
     finalist3.append(combinelist[y])
     del(combinelist[y])
finalist3[2] = 'Free Space'
for i in range(5):
     x = len(combinelist)
     y = random.randint(0,x-1)
     finalist4.append(combinelist[y])
     del(combinelist[y])
for i in range(5):
     x = len(combinelist)
     y = random.randint(0,x-1)
     finalist5.append(combinelist[y])
     del(combinelist[y])
finalist.append(finalist1)
finalist.append(finalist2)
finalist.append(finalist3)
finalist.append(finalist4)
finalist.append(finalist5)
print(tabulate(finalist))
#Functions are difficult to use
