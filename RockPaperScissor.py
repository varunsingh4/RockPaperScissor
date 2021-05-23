# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:33:58 2021

@author: 91760
"""
import random
Game = ["Scissor","Rock","Paper"]
comp = random.choice(Game)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock,Paper or Scissor:").capitalize()
    ##Conditions for rock paper scissor
    if player == comp:
        print("It's a tie")
    elif player =="Rock":
        if comp =="Scissor":
            print("You win!",comp,"smashes",player)
            player_score+=1
        else:
            print("You loose!",comp,"covers",player)
            cpu_score+=1
    elif player == "Scissor":
        if comp =="Rock":
            print('You lose!',comp,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cuts",comp)
            player_score+=1
    elif player == "Paper":
        if comp == "Scissor":
            print('You lose!',comp,"cuts",player)
            cpu_score+=1
        else:
            print('You win',player,'covers',comp)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break
            