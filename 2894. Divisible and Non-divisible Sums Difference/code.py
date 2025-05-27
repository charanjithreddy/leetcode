class Solution(object):
    def differenceOfSums(self, n, m):
        nums2=sum([i for i in range(1,n+1) if i%m==0]);
        return (n*(n+1))/2-nums2-nums2;
        """
        :type n: int
        :type m: int
        :rtype: int
        """

if(__name__=="__main__"):
    n = 10;
    m = 3;
    print(Solution().differenceOfSums(n,m))