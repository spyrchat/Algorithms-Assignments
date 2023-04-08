import random
import numpy as np


# Define the 15 names
names = ['Alice','Pavlos']

# Create an array of length 100 with 15 randomly repeated names
arr = np.array(random.choices(names, k=10)) 


#=== CheckIfPotentialWinner function has one for-loop hence the O(n) Complexity ===#
def checkIfPotentialWinner(candidate, arr):  # This function finds out if the candidate 
                                             # with has more than 50% of the votes
    counter  = 0
    for i in range(len(arr)):
        if arr[i] == candidate:
            counter = counter + 1
    if counter >= len(arr)/2 :
        return True
    else :
        return False

def findWinnerCandidate(votesArray):    # This function iterates through the votes array 
    n = len(votesArray)
    winner1 = 0       # Winner1 is the first candidate that has at least N/2 votes
    winner2 = 0       # Winner2 is the second candidate that has at least N/2 votes 
                      # (it exists only if there are two candidates and have half votes)
   
    for i in range(n):   # Here is the first for-loop that goes through the whole array
        if checkIfPotentialWinner(votesArray[i], votesArray):   
            if(winner1 != 0 and votesArray[i] != winner1):  # Check if  a winner exists
                winner2 = votesArray[i]
            else:
                winner1 = votesArray[i]
    if winner1 == 0 and winner2 == 0:
        print("No Candidate has the majority of the Votes")
        return None    
    elif winner1 != 0 and winner2 == 0:
        return winner1
    elif winner1 != 0 and winner2 != 0:
        print("The votes of the 2 Candidates are tied!")
        return winner1, winner2
#===== findWinnerCandidate function has a for-loop but inside calls a function with O(n) Complexity called 'checkIfPotentialWinner' so the Overall Complexity is O(n^2)

print(findWinnerCandidate(arr))

        
