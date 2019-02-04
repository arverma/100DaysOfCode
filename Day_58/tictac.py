# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:50:13 2019

@author: amanranjan

TicTac: Dumb System vs You

3x3 board is initialised with -1.
User: 0/O
System: 1/X

"""
import numpy as np
import random as r

class tictac_board():
    def __init__(self):
        self._board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    
    def display_board(self):
        #print(np.array(self._board))
        for i in self._board:
            for j in i:
                if(j == -1):
                    print("__", end = " ")
                else:
                    if(j == 0):
                        print("","O", end = " ")
                    else:
                        print("","X", end = " ")
            print()
    
    def compute(self, i, j):
        result = -1
        temp = np.array(self._board)
        # ___________Column Check_________________
        if(-1 not in temp[:,i]):
            #print("sum(temp[:,i])", sum(temp[:,i]))
            if(sum(temp[:,i]) == 0 or sum(temp[:,i]) == 3):
                return 1
        # ___________Row Check___________________
        if(-1 not in temp[i,:]):
            #print("sum(temp[i,:])"), sum(temp[i,:])
            if(sum(temp[i,:]) == 0 or sum(temp[i,:]) == 3):
                return 1
        # ___________Diagonal Check_________________
        if(i == j or i+j == 2):
            result = 0
            #_______________Top Left to Bottum Right Diagonal_________
            if(i == j):
                for i in range(3):
                    if(temp[i,i] == -1):
                        return -1
                    result +=  temp[i,i]
            #_______________Bottum Left to Top Right Diagonal
            else:
                for i in range(3):
                    if(temp[2-i,i] == -1):
                        return -1
                    result +=  temp[2-i,i]
                    
            #print(result)
            if(result == 0 or result == 3):
                return 1
        return -1
    
        
    #_____________System makes move____________
    def system(self):
        i, j = r.randint(0, 2), r.randint(0, 2)
        #1print(i, j)
        while(self._board[i][j] != -1):
            i, j = r.randint(0, 2), r.randint(0, 2) 
        self._board[i][j] = 1
        
        print("System")
        if(self.compute(i, j) == 1):
            print("-*|**|**|**|**|*--------System Won-----------*|**|**|**|**|**|*")
        
    #_____________User makes move____________
    def user(self):
        user_input = list(map(int, input("Input: Index[i][j] .... ").split()))
        i, j = user_input[0], user_input[1]
        self._board[i][j] = 0
        
        print("User")
        if(self.compute(i, j) == 1):
            print("-*|**|**|**|**|*--------You Won-----------*|**|**|**|**|**|*")
        
    def play(self):
        print("\n \t System Vs You")
        chance = int(input("Input: Who first? 1/0 .... "))
        
        choice = 1
        while(choice == 1):
            if(chance == 0):
                self.user()
                self.system()
                pass
            else:
                self.system()
                chance = 0
                pass
            self.display_board()
            #print("chance: ", chance)
            choice = int(input("Input: Play(1) / Abort(0): _____ "))


# Main Function           
game = tictac_board()
game.display_board()
game.play()
    