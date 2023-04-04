import random
import numpy as np

# Define the 15 names
names = ['Pavlos','Vougiouklaki']

# Create an array of length 100 with 15 randomly repeated names
arr = np.array(random.choices(names, k=10)) 
#==== findWinnerCandidate function uses Divide and Conquer Algorithm Design Technique and utilizes reccursion so we can find the reccurences in O(logn) time Complexity, We found The Reccurences and the subproblems using Master Theorem
def findOccurrences(arr, high, low, key):
    
    if(low == high and arr[low] == key):
        return 1
    
    if low > high or (low == high and arr[low]!= key):
        return 0
    

    left = findOccurrences(arr, (low+high)//2, low, key)
    right  = findOccurrences(arr, high, (high+low)//2 + 1, key)
    return left + right

def findMajority(arr):
    if len(arr)!=0:  
        temp1 = 'Nan'
        temp2 = 'Nan'
        print(arr)
        #Iterate through the array to find the Candidate with the 50% of the votes
        for i in range(len(arr)):
            if findOccurrences(arr,len(arr)-1,0,arr[i]) >= len(arr)/2 :
                temp1 = arr[i]
        #Iterate through the array again to make sure there isn't a second candidate that has 50% of the votes
        for j in range(len(arr)):
            if  findOccurrences(arr,len(arr)-1,0,arr[i]) == len(arr)/2 and arr[j] != temp1:
                temp2 = arr[j]
        
        if temp1 == 'Nan' and temp2 == 'Nan':
            print("No Candidate has the majority of the Votes")
            return None    
        elif temp1 != 'Nan' and temp2 == 'Nan':
            return temp1
        elif temp2 !='Nan' and temp1 != 'Nan':
            print("The votes of the 2 Candidates are tied!")
            return temp1,temp2
         
    else :
        print("No Voters Found")
    
#=== The findMajority function has two independent for-loops that each call a function called'findOccurences' with O(logn) Complexity,so the call of an O(logn) function inside the loop, makes the overall complexity O(nlogn) 

print(findMajority(arr))
    