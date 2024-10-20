def isSimilar(word1:str, word2:str)->bool:
    if len(word1) > len(word2):
        word1,word2=word2,word1
        
    word3=set(word2)
    # for word in word1:
    
    return True

class Solution:
    def similarPairs(self,words:list[str])->int:
        return 0

print(Solution().similarPairs(["aba","aabb","abcd","bac","aabc"]))