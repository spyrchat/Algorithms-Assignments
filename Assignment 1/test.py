from boyerMoore import announceWinners  

import numpy as np
import random


num_tests = 5
names = ['Alice','Pavlos']  
for i in range(num_tests):
    arr = np.array(random.choices(names, k=10))
    print(f"Test {i+1}: {announceWinners(arr)}")
    print(arr)
    count1 = 0
    count2 = 0
    count = 0
    if len(announceWinners(arr)) == 2:
        for elem in arr:
            winner1 = announceWinners(arr)[0]
            winner2 = announceWinners(arr)[1]
            if isinstance(winner1, tuple):
                if elem in winner1:
                    count1 += 1
            elif elem == winner1:
                count1 += 1
            
        for elem in arr:
            
            winner2 = announceWinners(arr)[1]
            if isinstance(winner2, tuple):
                if elem in winner2:
                    count2 += 1
            elif elem == winner2:
                count2 += 1
        print("winner 1 apppears " + str(count1) + " times")
        print("winner 2 apppears " + str(count2) + " times")
    else:
        for elem in arr:
            
            winner = announceWinners(arr)
            if isinstance(winner, tuple):
                if elem in winner:
                    count += 1
            elif elem == winner:
                count += 1
        print("winner apppears " + str(count) + " times")


    
    
    
		
		
   
