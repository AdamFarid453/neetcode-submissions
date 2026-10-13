class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}
        for words in strs:
            key = "".join(sorted(words))
            if key in sol:
                print(words)
                sol[key].append(words)
            else:
                sol[key] = [words]
        return [i for i in sol.values()]
