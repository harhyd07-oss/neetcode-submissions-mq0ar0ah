class Solution:
    def hasDuplicate(self, l: list[int]) -> bool:
        s=set(l)
        if len(s)==len(l):
            return False
        else:
            return True    