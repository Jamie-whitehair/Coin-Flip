
import random
try:
    flips_amount = int(input("How many times do you want to flip the coin? \n"))
    heads_tails = []
    chance = [0, 1]
    for x in range(flips_amount):
        flip = random.choice(chance)
        if flip == 0:
            heads_tails.append(0)
        elif flip == 1:
            heads_tails.append(1)
    heads = heads_tails.count(0)
    tails = heads_tails.count(1)
    print("You got %d heads and %d tails!" % (heads, tails))
    heads_result = heads / flips_amount 
    tails_result =  tails / flips_amount 
    tails_result *= 100
    heads_result *= 100
    print("You got %f percent heads and %f percent tails out of %d flips" % (heads_result, tails_result, flips_amount))
    input()
except Exception as x:
    print(x)
    input()
