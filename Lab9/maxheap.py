'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 04/25/2023
Lab: lab9
Last modified: 04/26/2023
Purpose: Contains a main function.
'''

#maxheap.py

from patienthandler import PatientHandler

#creates a max heap class
class MaxHeap:

    #initializes heap
    def __init__(self):
        self.maxHeap = []

    #add to heap
    def add(self, entry):
        self.maxHeap.append(entry)

        self.upheap(len(self.maxHeap)-1)

    #traverse upwards on heap
    def upheap(self, index):
        if index == 0:
            return True
        
        elif index > 0:
            if self.maxHeap[index] > self.maxHeap[(index-1)//2]:
                tempVar = self.maxHeap[index]

                self.maxHeap[index] = self.maxHeap[(index-1)//2]

                self.maxHeap[(index-1)//2] = tempVar

                self.upheap((index-1)//2)

            else:
                return True
            
        else:
            return False
    
    #prints heap
    def printMaxHeap(self):
        if len(self.maxHeap) == 0:
            print("There are no patients left")

        else:
            print(f"{self.maxHeap[0]}\n")
    
    #removes from heap
    def remove(self):
        if len(self.maxHeap) == 0:
            return None
        
        else:
            heapInitial = self.maxHeap[0]

            heapNew = self.maxHeap[-1]

            self.maxHeap[0] = heapNew

            self.maxHeap.pop()
            
            self.downheap(0)

            return heapInitial
    
    #traverse downwards on heap
    def downheap(self, index):
            right = 2 * index + 2

            left = 2 * index + 1

            if right < len(self.maxHeap) and self.maxHeap[right] > self.maxHeap[index]:
                index = right

            elif left < len(self.maxHeap) and self.maxHeap[left] > self.maxHeap[index]:
                index = left

            else:
                return True

    #count how many patients are left
    def count(self):
        return len(self.maxHeap)
