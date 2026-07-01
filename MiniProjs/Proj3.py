def GetAverageMarks(studRecs, name):
    if name in studRecs:
        marksLi = studRecs[name]
        avg = sum(marksLi) / len(marksLi)
        return avg
    else:
        return "Student not found."

gn = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")
res = GetAverageMarks(gn, name)

print("Average percentage mark: ", res)

'''O/P:
Enter a name: Krishna
Average percentage mark:  68.0
'''
