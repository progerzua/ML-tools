'''
https://www.codewars.com/kata/are-the-numbers-in-order
Pretty simple task
Just to practice my coding skills
'''

def in_asc_order(arr):
    for i in xrange(len(arr)):
        if i > 0 and arr[i-1] > arr[i]:
            return False
    return True