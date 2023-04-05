'''
Given 2 strings, return true if t is an anagram of s and false otherwise
'''

'''
Thought Process
Sort both inputs and compare (maybe lowercase the strings as well)
Time: O(nlogn)
Space: O(1)
'''

def isAnagram(s: str, t: str):
    return sorted(s) == sorted(t)

'''
While this does work for Python, it's probably cheating in most situations so I will try to do it in a more
algorithmic way

The idea is to...
1. Check if strings length are the same
    If not return False
2. Go through each string and put them into 2 separate hash maps
3. Compare both at the end

Time: O(n)
Space: O(n)
'''

def isAnagramAlgor(s: str, t: str):
    if len(s) != len(t):
        return False
    
    sMap, tMap = {}, {}

    for i in range(len(s)):
        sMap[s[i]] = 1 + sMap.get(s[i], 0)
        tMap[t[i]] = 1 + tMap.get(t[i], 0)
    
    return sMap == tMap
        

print(isAnagramAlgor('anagram', 'nagaram'))