class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # loop through s and store each letter and occurrence in a hashtable
        # loop through t and store each letter and occrence in a hashtable
        # return s == t at the end
        hash_map = {}
        if len(s) != len(t):
            return False
        # do it for s
        for letter in s:
            if letter not in hash_map:
                hash_map[letter] = 1
            else:
                hash_map[letter]+=1
        # do it for t
        for letter in t:
            if letter not in hash_map:
                # if its a new letter we dont want it
                return False
            else:
                hash_map[letter]-=1

        return all(count == 0 for count in hash_map.values())