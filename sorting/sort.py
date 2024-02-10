#This program contains the algorithms that are used to sort


class Sort:

    def bubble(list1: list[int], length: int):

        listSorted = False
        changes = []
        
        run = 0 #represents the numbers of runs through
        list1

        while not listSorted:
            changes.append(0) #used to check if there is a runthrough with no swaps

            for i in range(length - run - 1): #makes use of a secured value

                if list1[i] > list1[i+1]: #i is never the last value, as i+1 would not always work
                    #swap two numbers
                    temp = list1[i+1]
                    list1[i+1] = list1[i]
                    list1[i] = temp
                    changes[run] += 1

                else: #leave the same
                    pass
            
            run += 1

            if changes[run-1] == 0: #if there were no changes last time
                listSorted = True
            elif 1 + run == length: #if the list has only one working value
                listSorted = True
            else:
                pass
        
        return list1
    

    def insertion(list1: list[int], length: int):

        listSorted = False
        index = 0

        """sortedList = []
        for i in range(length):
            sortedList.append("")"""
        
        while not listSorted:

            for i in range(index + 1): #loops for as long as there are placements + 1

                if i == index: #if the place we are inspecting is the position of it already
                    # leave the same
                    pass

                elif list1[index] <= list1[i]: #if it needs to be placed
                    # everything after is shuffle up by a place
                    temp = list1[index]
                    list1[i + 1:index + 1] = list1[i:index]
                    # insert in place
                    list1[i] = temp
                    break
            
            index += 1 #looking at the next place in the list now

            if index == length: #once all places have been filled in
                listSorted = True

        return list1


    def merge(list1: list[int], length: int):

        if len(list1) <= 1: #once list has been broken down into a single component
            return list1
        
        else: #split list in half (or as half as possible)
            midpoint = length // 2
            left = list1[0:midpoint]
            right = list1[midpoint:length+1]

            leftList = Sort.merge(left, midpoint) #at first whatever gets out of here is single...
            rightList = Sort.merge(right, length + 1 - midpoint) #... then they get combined

            #method of combining the lists
            outputList = [] #this will be returnned

            while len(leftList) > 0 or len(rightList) > 0: #until both are zero

                if len(leftList) == 0: #once the leftList has no more items, move all of the right list to output
                    outputList.append(rightList[0])
                    rightList = rightList[1:len(rightList)+1]

                elif len(rightList) == 0: #once the rightList has no more items, move all of the left list to output
                    outputList.append(leftList[0])
                    leftList = leftList[1:len(leftList)+1]

                elif leftList[0] <= rightList[0]: #when the first of leftList is less than or equal to the first
                                                  #..of rightList, append to output list
                    outputList.append(leftList[0])
                    leftList = leftList[1:len(leftList)+1]
                else:                             #when the first of rightList is less than or equal to the first
                                                  #..of leftList, append to output list
                    outputList.append(rightList[0])
                    rightList = rightList[1:len(rightList)+1]

            return outputList


    def quick(list1: list[int], length: int):

        pivotIndex = length // 2

        if length != 0:
            pivot = list1[pivotIndex] #can only generate a pivot if the list has contents

        leftList = [] #lower than the pivot
        rightList = [] #greater than the pivot
        if length == 0:
            return [] #returns nothing when the length is 0
        elif length > 2:
            listWithoutMidpoint = list1[0:pivotIndex]+list1[pivotIndex+1:length] #so that the pivot isnt copied
            for item in listWithoutMidpoint: #sorts into left and right
                if item <= pivot:
                    leftList.append(item)
                else:
                    rightList.append(item)

            leftList = Sort.quick(leftList, len(leftList)) #recursively calls quick sort on each new list
            rightList = Sort.quick(rightList, len(rightList)) #recursively calls quick sort on each new list

        elif length == 2: #special case for length of 2 - no need to call recursive
            if list1[0] <= pivot:
                leftList.append(list1[0])
            else:
                rightList.append(list1[0])
        
        else: #list length is one
            pass

        return leftList + [pivot] + rightList
