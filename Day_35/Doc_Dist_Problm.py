# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:53:08 2018

################################################
#    Excution time in my laptop: 0.364 Sec     #
################################################

@author: amanranjan
"""
import time
start = time.time()


##   Rading file bobsey.txt and lewis.txt
d1 = open("lewis.txt", "r")
f1 = d1.read().lower()
d2 = open("bobsey.txt", "r") 
f2 = d2.read().lower()
d1.close()
d2.close()
##   Removing all the symbols and converting them into list
import re
import numpy as np
f1 = re.sub(r'[^\w]', ' ', f1)
f2 = re.sub(r'[^\w]', ' ', f2)
f1 = f1.split()
f2 = f2.split()
##   Putting the words into Dictionary with occurance count
dict_f1 = {}
for i in f1:
    if(i in dict_f1.keys()):
        dict_f1[i] += 1
    else:
        dict_f1[i] = 1
        
dict_f2 = {}
for i in f2:
    if(i in dict_f2.keys()):
        dict_f2[i] += 1
    else:
        dict_f2[i] = 1
##   Finding dot Product
score = 0
for i in dict_f1.keys():
    score += dict_f1[i]*dict_f2.get(i,0)
##   Normalising
print("Similarity Score: ", score/(np.sum(np.array(list(dict_f1.values()))**2)**0.5 * np.sum(np.array(list(dict_f2.values()))**2)**0.5))
##   Taking cos Inverse
print("Distance between File1 and File2 is: ", np.arccos(score/(np.sum(np.array(list(dict_f1.values()))**2)**0.5 * np.sum(np.array(list(dict_f2.values()))**2)**0.5)))

##   Printing Execution Time
end = time.time()
print("Time Taken = ", end - start, "Sec")















