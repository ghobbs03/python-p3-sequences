#!/usr/bin/env python3

def print_fibonacci(length):
    if (length == 0):
        print([])
        return

    array = [None]*(length+1)
    array[0] = 0 #first
    array[1] = 1 #second

    for i in range(2, length+1):
        array[i] = array[i-1] + array[i-2] # 1 + 1
        
    print(array[:length])