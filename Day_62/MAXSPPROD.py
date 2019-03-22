# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 15:37:19 2019

@author: amanranjan
"""
class Solution:
    def _first_greater(self, A, prev=True):
        stack = list()
        ans = [0] * len(A)
        
        if(prev):
            it = range(len(A))  
        else: 
            it = range(len(A)-1, -1, -1)

        for i in it:
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            ans[i] = stack[-1] if stack else 0
            stack.append(i)
        return ans

    def maxSpecialProduct(self, A):
        left = self._first_greater(A)
        right = self._first_greater(A, prev=False)
        maxx = - 1
        print(A)
        print(left) 
        print(right)

        for l, r in zip(left, right):
            maxx = max(l * r, maxx)
        return maxx % 1000000007
    
run = Solution()
print(run.maxSpecialProduct([ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ]))