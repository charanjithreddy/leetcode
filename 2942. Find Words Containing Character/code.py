class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i in range(len(words)) if (x in words[i])];
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

if(__name__=="__main__"):
    words = ["leet","code"];
    x = "e"
    print(Solution().findWordsContaining(words,x));