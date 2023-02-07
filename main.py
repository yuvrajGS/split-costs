def readInput(fin):
    items = {}
    itemList = fin.split("\n")
    for itemIN in itemList:
        item = itemIN.split(",")
        items[item[0]]= [float(item[1].strip()), "yuvraj", "meer", "thenu","cynthia","sarah"]
    return items

def optOut(items,yIN,mIN,tIN,cIN,sIN):
    for f in [yIN,mIN,tIN,cIN,sIN]:
        if id(f) == id(yIN):
            name = "yuvraj"
        elif id(f) == id(mIN):
            name = "meer"
        elif id(f) == id(tIN):
            name = "thenu"
        elif id(f) == id(cIN):
            name = "cynthia"
        elif id(f) == id(sIN):
            name = "sarah"
        for item in f:
            items[item].remove(name)
    return

def calCost(items):
    names = {"yuvraj": 0, "meer": 1, "thenu": 2,"cynthia":3,"sarah":4}
    finalCost=[0]*5
    for item in items:
        if (len(items[item]) == 6):
            for i in range(5):
                finalCost[i]+=(items[item][0])/5
        elif (len(items[item]) == 1):
            print("ERROR: Everyone opted out")
            break
        else:
            for i in range(1,len(items[item])):
                finalCost[names[items[item][i]]]+=(items[item][0]/(len(items[item])-1))

    return finalCost

def main(fIN,yIN,mIN,tIN,cIN,sIN):
    total=0
    items = readInput(fIN)
    optOut(items,yIN,mIN,tIN,cIN,sIN)
    finalCost=calCost(items)
    for i in finalCost:
        total+=i
    
    return finalCost, total
