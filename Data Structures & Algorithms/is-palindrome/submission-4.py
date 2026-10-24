class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ord() < 128 for non ascii characters
        new_text = "".join([char for char in s if char.isalnum()]).lower()
        i,j = 0, len(new_text)-1

        while i <= j:
            if new_text[i] == new_text[j]:
                i+=1
                j-=1
            else:
                return False
        return True