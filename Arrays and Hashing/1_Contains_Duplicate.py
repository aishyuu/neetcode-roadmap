'''
Problem: Given an integer of arrays
Return True if any value appears twice in the array
Return False if every element is distinct
'''

'''
Thought Process
Making 2 arrays and looping through them would really suck
That approach can easily become really bad due to a potential O(n^2)

Instead, we can make a dictionary (hash table) and check if the key exists
If the key exists in the dictionary, then that must mean we passed the value before, thus returning True
However, if it's not, we put it in the dictionaty with a random value to make the key exist in the dictionary
Loop this and if there is no True return at the end, return False
This would make the process go from O(n^2) to a O(n) max
'''


def containsDuplicate(arr):
    currentNums = {}
    for num in arr:
        if num in currentNums:
            return True
        else:
            currentNums[num] = 1
    
    return False

print(containsDuplicate([1,2,3,1]))