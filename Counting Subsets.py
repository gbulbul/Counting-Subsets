# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 00:24:01 2024

@author: gbulb
"""
class find_subsets:
    def subsets(n):
        tuples_one,tuples_two,tuples_three,tuple_for_null,combined=[],[],[],[0],0
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                for k in range(1,n+1,1):
                    if i!=j and i!=k and j!=k:
                       tuples_three=[(i,j,k)] #1
                       tuples_two=[(i,j),(i,k),(j,k)] #3
                       tuples_one=[(i),(j),(k)] #3
                       combined=len(tuples_three)+len(tuples_two)+len(tuples_one)+len(tuple_for_null)
        return print(combined)

if __name__=="__main__":
    n=3    
    find_subsets.subsets(n)
               