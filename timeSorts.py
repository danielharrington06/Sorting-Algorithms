from sorting import Sort
from sorting import Generate

import time

volume = 1000 # volume of the test (how many times the algorithms have to sort)
length = 50 # length of each sort (how many numbers are in each sort)

results = [] # method  of storing results
numSorts = 4 # number of sorting algorithms
decimalPlaces = 3 #how many decimal places to show for the results

for i in range(numSorts):
    results.append(0)

for i in range(volume):

    times = []

    #Generate(lower, upper, length)
    listOfData = Generate(-100, 100, length).random()

    times.append(time.time())
    sortedListOfData = Sort.bubble(listOfData[:], len(listOfData))
    times.append(time.time())
    sortedListOfData = Sort.insertion(listOfData[:], len(listOfData))
    times.append(time.time())
    sortedListOfData = Sort.merge(listOfData[:], len(listOfData))
    times.append(time.time())
    sortedListOfData = Sort.quick(listOfData[:], len(listOfData))
    times.append(time.time())

    

    for i in range(len(results)):
        results[i] += ((times[i+1] - times[i])*1000)



print()
print("The lists have been sorted.")
print(f"Volume: {volume}")
print(f"Length: {length}\n")
print(f"Bubble Sort took an average of {results[0]/volume:.{decimalPlaces}f}ms")
print(f"Insertion Sort took an average of {results[1]/volume:.{decimalPlaces}f}ms")
print(f"Merge Sort took an average of {results[2]/volume:.{decimalPlaces}f}ms")
print(f"Quick Sort took an average of {results[3]/volume:.{decimalPlaces}f}ms")
print()
