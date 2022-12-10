
# Import the random module
import random

def rps(move2):
    # Define the possible moves
    moves = ["rock", "paper", "scissors"]

    # Prompt player 1 for their move
    print("ROCK, PAPER, SCISSORS GO!")
    print(" ")
    print("Input one of the following: rock / paper / scissors")
    print(" ")

    player1 = input("So what's your move? ")
    player2 = move2

    # Check that player 1's move is valid
    while player1 not in moves:
        print(" ")
        print("That's not a rock or paper or scissors!")
        print(" ")
        print("Input one of the following: rock / paper / scissors")
        print(" ")
        player1 = input("So what's your move? ")

    
    if player1 == player2:
        return "tie", player1, player2
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
        return "p win", player1, player2
    else:
        return "c win", player1, player2

def strat(oldMove, currMove):
    
    if(oldMove == currMove):
        return "S"

    elif((oldMove == "rock" and currMove == "scissors") or (oldMove == "paper" and currMove == "rock") or (oldMove == "scissors" and currMove == "paper")):
        return "U"
    else:
        return "D"


def moveGenerator(oldMove, strat):

    if(strat == "S"):
        if(oldMove == "rock"):
            return "paper"
        elif (oldMove == "paper"):
            return "scissors"
        else:
            return "rock"
    
    elif(strat == "U"):
        if(oldMove == "rock"):
            return "rock"
        elif(oldMove == "paper"):
            return "paper"
        else:
            return "scissors"
        
    else:
        if(oldMove == "rock"):
            return "scissors"
        elif(oldMove == "paper"):
            return "rock"
        else:
            return "paper"

    