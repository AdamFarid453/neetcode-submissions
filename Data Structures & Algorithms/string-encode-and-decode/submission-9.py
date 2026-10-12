class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs: return []
        # res = ""
        # for i,s in enumerate(strs):
        #     res+=s
        #     if i != len(strs)-1:
        #         res+=' '
        # print(res)
        # return res
        res = ""
        for word in strs:
            res = res + f'{len(word)}#{word}'
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        ans = []
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
        return ans
