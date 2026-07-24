class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(word1) and pointer2 < len(word2):
            res = res + word1[pointer1]
            res = res + word2[pointer2]

            pointer1 += 1
            pointer2 += 1
        
        while pointer1 < len(word1):
            res = res + word1[pointer1]
            pointer1 += 1

        while pointer2 < len(word2):
            res = res + word2[pointer2]
            pointer2 += 1

        return res