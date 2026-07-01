def FindSecretMessage(filePath):
    fileObj = open(filePath, "r")
    linesLi = fileObj.readlines()
    fileObj.close()
    
    lineCount = len(linesLi)
    if lineCount > 12:
        meetingTime = lineCount - 12
        timePeriod = "PM"
    else:
        meetingTime = lineCount
        timePeriod = "AM"
        
    freqMap = {}
    for line in linesLi:
        cleanedLine = line.replace(".", " ").replace(",", " ").replace('"', " ")
        wordsLi = cleanedLine.split()
        for word in wordsLi:
            if word not in freqMap:
                freqMap[word] = 1
            else:
                freqMap[word] = freqMap[word] + 1
                
    maxCount = -1
    mostFrequentWord = ""
    
    for word in freqMap:
        if freqMap[word] > maxCount:
            maxCount = freqMap[word]
            mostFrequentWord = word
            
    print("Meeting time:", meetingTime, timePeriod)
    print("Meeting place:", mostFrequentWord, "Street")

ip = input("Enter the message: ")
FindSecretMessage(ip)

'''O/P:
Meeting time: 9 AM
Meeting place: Park Street
'''
