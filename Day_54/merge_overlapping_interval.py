# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:46:11 2019

@author: amanranjan
"""
def merge(a):
    a = [list(i) for i in a]
    a = sorted(a, key = lambda x:x[0])
    print(a)
    temp = [0,0]
    flag = 0
    res = []
    for i in range(len(a)-1):
        if(a[i][1] >= a[i+1][0]):
            if(flag == 0):
                temp[0] = a[i][0]
            a[i+1][1] = max(a[i][1], a[i+1][1])
            temp[1] = a[i+1][1]
            flag = 1
            print(i, temp, a)
        else:
            print(i, temp, res)
            if(flag == 1):
                res.append(temp)
                temp = [0, 0]
            else:
                res.append(a[i])
            flag = 0
    if(flag == 1):
        res.append(temp)
    elif(a[i][1] < a[i+1][1]):
        res.append(a[i+1])
    return res

a = [[2,3],[11,12],[1,10]]
print(merge(a))



# =============================================================================
# bool comp_sort(Interval a,Interval b){
#      return a.start<b.start;
#  }
# vector<Interval> Solution::merge(vector<Interval> &A) {
#     sort(A.begin(),A.end(),comp_sort);
#     vector<Interval> res;
#     int n=A.size();
#     res.push_back(A[0]);
#     for(int i=1;i<n;i++){
#         if(A[i].start<=res[res.size()-1].end)
#          res[res.size()-1].end=max(res[res.size()-1].end,A[i].end);
#         else
#          res.push_back(A[i]);
#     }
#     return res;
# }
# =============================================================================
