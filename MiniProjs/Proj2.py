def GetRunnerUpScore(scores):
    unique = set(scores)
    sortedLi = sorted(list(unique))
    
    if len(sortedLi) >= 2:
        return sortedLi[-2]
    else:
        return "Cant determine runner up"

li = [2, 3, 6, 6, 5]
runnerUp = GetRunnerUpScore(li)

print("Sample Input: ", li)
print("Sample Output: ", runnerUp)

'''O/P:
Sample Input:  [2, 3, 6, 6, 5]
Sample Output:  5
'''
