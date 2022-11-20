def readInput():
    items = {}
    f = open("input.txt", "r")
    for x in f:
        item = x.split(",")
        items[item[0]]= [float(item[1].strip()), "yuvraj", "meer", "thenu","cynthia","sarah"]
    f.close()
    return items

def optOut(items):
    for name in ["yuvraj", "meer", "thenu","cynthia","sarah"]:
        f = open(name+".txt","r")
        for x in f:
            item = x.strip()
            items[item].remove(name)
        f.close()
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

def main():
    count=0
    total=0
    items = readInput()
    optOut(items)
    calCost
    finalCost=calCost(items)
    for i in items:
        count+=items[i][0]
    print("Total = {:.2f}".format(count))
    print("Split costs:")
    print("Yuvraj = {:.2f}".format(finalCost[0]))
    print("Meer = {:.2f}".format(finalCost[1]))
    print("Thenu = {:.2f}".format(finalCost[2]))
    print("Cynthia = {:.2f}".format(finalCost[3]))
    print("Sarah = {:.2f}".format(finalCost[4]))
    for i in finalCost:
        total+=i
    print(total)

        

main()

