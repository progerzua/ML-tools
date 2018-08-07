'''
https://www.codewars.com/kata/equal-sides-of-an-array
'''

def find_even_index(arr):
    sums = [0, 0] # index 0 = left; index 1 = right
    
    # first step
    sums[1] = sum(arr[1:])
    if sums[0] == sums[1]:
        return 0
    
    indx = -1
    for i in range(1, len(arr)):
        sums[0] = sums[0] + arr[i - 1]
        sums[1] = sums[1] - arr[i]
        if sums[0] == sums[1]:
            indx = i
            break
    return indx