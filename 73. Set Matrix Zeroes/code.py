class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix);
        n=len(matrix[0]);
        r=set();
        c=set();
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    r.add(i);
                    c.add(j);
        for i in r:
            for j in range(n):
                matrix[i][j]=0;
        for i in range(m):
            for j in c:
                matrix[i][j]=0;

if (__name__=="__main__"):
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]];
    print("input");
    for i in matrix:
        print(i);
    print();
    print("output");
    Solution().setZeroes(matrix);
    for i in matrix:
        print(i);