class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        max_num = 0
        i,j=0,0

        while j < len(s):
            if s[j] not in x:
                x.add(s[j])
                j+=1
                max_num = max(max_num, j-i)
            else:
                x.remove(s[i])
                i+=1
        return max_num
            

        