import random
import numpy as np

#====== Define the pool of names =======#
names = ["Spiros","Pavlos","Christina",]

#======= Create an array of length k with len(names) randomly repeated names ======#
arr = np.array(random.choices(names, k=100000)) 

#====== initializes an empty dictionary to store the frequencies of the HASHED values of the array with Time Complexity O(n) =======#
def CountOccurrences(arr):
    freq = {}                  
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] = freq[arr[i]] + 1
        else:
            freq[arr[i]] = 1
    return freq


#======= Find the key for value val using dict.keys() method with time Complexity O(n) ======#
def FindKey(my_dict,val):
    for key in my_dict.keys():
        if my_dict[key] == val:
            return key
    return None  # value not found

def FindMajority(arr):
#== Check If the given array is not empty ===#    
    if len(arr)==0:
        print("The array with the votes cannot be empty")
        return None
#=== We will use a dictionary so we can identify with the unique elements of the array and assign to each unique element an integer ===# 
    d = {}       
#=== initializes hash as a list of zeroes of length = len(arr), sets both possible winners to -1, counter to zero and tie to FALSE ===#
    hash = [0] * len(arr)   
    max1 = -1 
    max2 = -1
    ctr = 0
    tie = 0
    
    for i in range(len(arr)):
        if arr[i] not in d:     #checks if the element does not exist in the dictionary 
            d[arr[i]] = ctr    
            ctr = ctr + 1       #Essentially ctr Contains the number of the Candidates ranging from 0 to n
    
    for j in range(len(arr)):
        hash[j] = d[arr[j]]     #Encodes the string values of the arr to integers in another identical array
    
    freq = CountOccurrences(hash)

#=====Iterates through the freq dictionary to find the Candidate with the Majority of the Votes========#
    for k in range(0,ctr):
        if freq[k] > len(arr) / 2:         
            max1 = k
        if freq[k] == len(arr) / 2:
            if(k != max1 and tie == 1):
                max2 = k
            else:
                max1 = k
            tie = 1

    
    if max1 != -1 and max2 != -1:
        temp1 = FindKey(d,max1)
        temp2 = FindKey(d,max2)
        return temp1,temp2

    
    if tie == 0 and max1 != -1:
        return FindKey(d,max1)
    
    if max1 == -1 and max2 == -1:
        print("No Candidate has the Majority of Votes")
    
#===== The FindMajority function calls two Functions with Time Complexity O(n) each and has three independent for loops with time complexity O(n)each, so Overall Time Complexity is O(n) ====#
print(FindMajority(arr))
