from sorting import Sort
from sorting import Generate

error = 0

volume = 100 #how many tests should be carried out
length = 10 #length of each test

for i in range(volume):
    #Generate(lower, upper, length).random()
    listOfData = Generate(1, 100, length).random()

    sortedListOfData = Sort.insertion(listOfData[:], len(listOfData))

    print(listOfData, "=>", sortedListOfData)
    listOfData.sort()

    if sortedListOfData != listOfData:
        error += 1
        print("^^ ERROR ^^\n")
    else:
        pass
    

print(f"{volume - error} out of {volume} sorts passed.")