# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:55:36 2019

@author: amanranjan
"""

def triplet(a):
    a = list(map(float, a))
    
    if(len(a) < 3 or sum(a) <= 1 or min(a) >= 2):
        return 0
    else:
        trip = []
        for i, x in enumerate(a):
            if(i < 2):
                trip.append(x)
            else:
                trip.append(x)
                #print(trip, sum(trip))
                if(sum(trip) >=2 ):
                    trip.remove(max(trip))
                elif(sum(trip) <= 1 ):
                    trip.remove(min(trip))
                else:
                    return 1
                #print(trip)
    return 0

#a = ["2.673662", "2.419159", "0.573816", "2.454376", "0.403605", "2.503658", "0.806191"]
#a = ["2.445610", "0.129967", "2.376455", "1.910948", "0.917844", "0.815911", "1.743973"]
a = ["0.628934", "0.939859", "0.898308", "1.251313", "1.380492", "1.070370", "0.701036", "1.349819", "1.277858", "1.171202"]
#a = ["0.2", "0.3", "1.4"]

print(triplet(a))