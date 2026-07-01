def ProcessPurchaseFile(filePath):
    try:
        fileObj = open(filePath, "r")
        linesLi = fileObj.readlines()
        fileObj.close()
        
        purchasedCount = 0
        freeCount = 0
        totalAmount = 0
        discountAmount = 0
        
        for line in linesLi:
            cleanedLine = line.strip()
            if not cleanedLine:
                continue
                
            partsLi = cleanedLine.split()
            if len(partsLi) < 2:
                continue
                
            itemName = partsLi[0]
            priceVal = partsLi[1]
            
            if itemName.lower() == "discount":
                discountAmount = int(priceVal)
            elif priceVal.lower() == "free":
                freeCount = freeCount + 1
                purchasedCount = purchasedCount + 1
            else:
                totalAmount = totalAmount + int(priceVal)
                purchasedCount = purchasedCount + 1
                
        finalAmount = totalAmount - discountAmount
        
        print("No of items purchased:", purchasedCount)
        print("No of free items:", freeCount)
        print("Amount to pay:", totalAmount)
        print("Discount given:", discountAmount)
        print("Final amount paid:", finalAmount)
        
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")

ip = input("Enter the file name: ")
ProcessPurchaseFile(ip)

'''O/P:
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130'''
