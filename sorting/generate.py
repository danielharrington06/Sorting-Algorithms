#This program generates a list of numbers between n and m values with length l
import random


class Generate:
    def __init__(self, lower: int, upper: int, length: int) -> list[int]:
        self.lower = lower
        self.upper = upper
        self.length = length
    
    def random(self):
        list1 = []

        for i in range(self.length):
            list1.append(random.randint(self.lower, self.upper))
        
        return list1