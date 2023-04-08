import random
import numpy as np


# Define the Ν names
#names = ['Alice','Pavlos']

# Create an array of length k with N randomly repeated names
# arr = np.array(random.choices(names, k=10))


#This Function is a variation of the Boyer-Moore Majority Algorithm that takes and array as input and finds the most popular element in O(n) Complexity
def findCandidate(arr):
    if len(arr) != 0:
        candidate = -1
        votes = 0

        for i in range(len(arr)):
            if votes == 0:
                candidate = arr[i]
                votes = 1
            else :
                if arr[i] == candidate:
                    votes = votes + 1
                else:
                    votes = votes - 1
        return candidate
    else:
        print("The input array cannot be of zero length")
        return None
 
  
#This Function Checks if The most popular Element of the Array also has the Majority in O(n) complexity
def checkForMajority(candidate,array):
    ctr = 0
    for j in range(len(array)):
        if array[j] == candidate:
            ctr = ctr + 1
    if ctr >= len(array) / 2:
        return True
    else :
        return False
    
#This Function is needed to cover the case that 2 winners exist It creates a new array without the candidate element the previous functions calculated, and checks for a second Candidate, then Checks if The 2nd Candidate has 50% of the Votes 
def announceWinners(arr):
    cnd = findCandidate(arr)
#    print(cnd)
#    print(arr)
    if checkForMajority(cnd,arr) == True:
        arr2 = []
        for i in range(len(arr)):
            if arr[i] != cnd:
                arr2.append(arr[i])

        cnd2 = findCandidate(arr2)
        if checkForMajority(cnd2,arr) == True:
            return cnd,cnd2
        else :
            return cnd
    else:
        return None        
        
       

#print(announceWinners(arr))

