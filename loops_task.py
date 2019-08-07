print("LOOPS TASK")
print("Cashier System")
print("--------------------------")

items =[]
dict = {}
y1 = ""
y2 = ""
y3 = ""
x1 = 0
x2 = 0
total = 0

while True:
    item = input("item (enter \"done\" when finished): ")
    if item != "done":
        price = input("price: ")
        quantity = input("quantity: ")
        dict ['item'] = item
        dict ['price'] = price
        dict ['quantity'] = quantity
        items.append(dict.copy())
    else:
        break
    #items.append(dict)
#print(dict)
#print(items)
print("--------------------------")
print("receipt")
print("--------------------------")

for i in items:
    for key in i:
        if key == 'price':
            x1 = float(i[key])
            y1 = i[key]
        elif key == 'quantity':
            x2 = float(i[key])
            y2 = i[key]
        elif key == 'item':
            y3 = i[key]
    total += float(x1*x2)
    print ("%d %s %.3fKD" % (x2, y3,(x1*x2)))
    #print (y2 + " " + y3 + " " + str(x1*x2) + "KD")
     
      
print("--------------------------")
#print("total: " + str(total))
print("Total: %.3f " % total)
print("\nEND")
