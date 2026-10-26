class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        h_map = {}
        for i in nums:
            if i in h_map:
                h_map[i] +=1
            else:
                h_map[i] = 1
        res = []
        count=0
        x = sorted(h_map.items(),key=lambda item: item[1], reverse=True)
        for i,j in x:
            print(res)
            res.append(i)
            count+=1
            if count == k:
                return res
        
        