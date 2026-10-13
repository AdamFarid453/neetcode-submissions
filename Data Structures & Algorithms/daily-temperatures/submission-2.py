class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack approach
        # loop through and add next number to stack
        # if its greater then pop it out and return index difference
        # when we pop the element from the stack we know we reached the next num
        stack = []
        res = [0] *len(temperatures)
        for temps in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[temps]:
                last_index= stack.pop()

                res[last_index] = temps - last_index
            stack.append(temps)
            
        return res
            
        