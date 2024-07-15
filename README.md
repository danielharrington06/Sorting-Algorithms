# Sorting-Algorithms
A creation of bubble, insertion, merge and quick sort in python. I also made code to test that they all work and code to time them on different scales of input and sample sizes.

### Structure of Files
The algorithms are called from >sorting >sort.py and they are in the class Sort. 

The arrays are called from >sorting >generate.py and they are in the class Generate. 

In order to use a sorting algorithm or generate numbers, a file should be in the sorting algorithms directory and contain either ```from sorting import Sort``` or ```from sorting import Generate``` as needed.

## Set Up/Testing Programs

### checkSorts.py
This program was useful in testing and debugging the algorithms as I wrote them. 

You specify the volume (number of tests to carry out) and length of each test array. It then generates the sorts, tests them and shows the results. 

It tracks how many errors come up; this is where the outputted list is not equal to the sorted copy of the list, using python's ```.sort()``` function.

### timeSorts.py
This program tests and calculates the average run time of the different sorts, when they all sort the same arrays. 

You can again specify the volume and length of the test. It generates a array of numbers which it then calls each sorting algorithm to sort. It tracks the times and then does the necessary calculations to discover which is fastest on average.

It is assumed that all the sorting algorithms work correctly as there is no error checking in this program. 

### generate.py
This program generates a array of number within the range lower and upper of a specified length. It uses the random module in python and it can create arrays with repeated numbers in it. This is of course intended, as a real life application of ordering needs to deal with this.

It is called using ```Generate(lower, upper, length).random()```

## Sorting Algorithms

### sort.py
The sorting algorithms are all located in >sorting >sort.py in the class Sort. They are all programmed to sort into ascending (a.k.a non decreasing) order. It would be easy enough to flip the array with a fairly simple function if this was ever needed.

A sort is called using ```Sort.sortType(list, length)``` where ```sortType``` is either bubble, insertion, merge, or quick.

### Bubble Sort
Bubble sort, like the name suggests 'bubble' up the array, comparing ```number[i]``` with ```number[i+1]``` and swaps them if ```number[i]``` is greater than ```number[i+1]```. It does this up the length of the array and then repeats it, from the bottom (left) of the array. The rightmost value from each 'run' gets locked in place as it has to be the biggest from that run.

This algorithm is simple to implement and very space efficient, but not very time efficient.

Time Complexity: $$O(n^2)$$
Space Complexity: $$O(1)$$

### Insertion Sort
Insertion sort builds a sorted array by comparing values in the unsorted section of the array to those in the sorted section of the array and inserts it in the appropriate place. It does one run through of the array which can include runs through the sorted section of the array to determine the correct place.

This algorithm is preferred for arrays of few elements or mostly sorted arrays as it can practically skip the sorted values. It is efficient in terms of space.

Time Complexity: $$O(n^2)$$
Space Complexity: $$O(1)$$

### Merge Sort
Merge sort recursively splits the unsorted array down into individual arrays and then combines the arrays, considering the leftmost items of both lists and then removing the elements once merged. It returns this to the instance of the method from which it was called. This repeats up until the list is fully returned and sorted.

This algorithm is more complicated to implement but is very time efficient. However, it can be less space efficient than other algorithms as it splits up each array into individual elements.

Time Complexity: $$O(n log n)$$
Space Complexity: $$O(n)$$

### Quick Sort
Quick sort selects a pivot point (often the middle, although it can be any number in the array, as long as it is consistent). It then moves all the numbers less than or equal to the pivot number to the left (unordered) and greater than to the right. It repeats this process for the new arrays to the left and to the right, so works recursively until all resulting arrays have only one item. The one item arrays get combined into the outputted array.

This algorithm is one of the msot efficient algorithms and it is relatively easy to implement. However, it is sensitive to the choice of the pivot; this means that the pivot choice, when always the middle could be very or not very efficient. In my implementation, I was only able to achieve a less efficient than possible time complexity, but with research and thinking, I could improve this.

Time Complexity: $$O(log n)$$
Space Complexity: $$O(n log n)$$

## Information about Big O notation used
The stated time complexities refer to the average case, but in bubble, insertion, and merge, the average case is equivalent to the worst case.

The stated space complexities refer to the worst case, but in all the algorithms, this is equivalent to the average case.

Furthermore, I have had to teach myself about Big O notation as I have not yet covered this in my A Level Computer Science course, so some may be incorrect. Please forgive me if this is the case.
