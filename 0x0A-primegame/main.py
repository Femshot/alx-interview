#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
#from chat_gpt_prime_game import isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3]))) # Winner: Ben

print("Winner: {}".format(isWinner(3, [4, 5, 1]))) # Winner: Ben
