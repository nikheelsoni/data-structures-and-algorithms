# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:58:19 2022

@author: nikheel
"""

class MyCircularQueue():
    
    def __init__(self,k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
        
    def enqueue(self, data):
        
        if ((self.tail + 1) % self.k == self.head):
            print ("The circular queue is full")
            
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            
    def dequeue(self):
        # if empty
        if self.head == -1:
            print ("Circular queue is empty")
    
        # if one element
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
        
    def printCQueue(self):
        if (self.head) == -1:
            print ("No element in the circular queue")
            
        elif(self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end = " ")
            print()
        else:
            for i in range(self.head, self.k):
                print (self.queue[i], end = " ")
            for i in range(0, self.tail + 1):
                print (self.queue[i], end = " ")
            print ()
            
obj = MyCircularQueue(5)
obj.enqueue(1)

print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
        