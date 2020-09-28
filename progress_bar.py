from tqdm import tqdm
from random import randint

# heads = 0
# tails = 0

# for i in tqdm(range(100000000), desc='Coin Flip Progress'):
#     toss = randint(0, 1)
#     if toss == 0:
#         heads += 1
#     else:
#         tails += 1


num_games = 3

for game in tqdm(range(num_games), desc='Overall Progress'):
    heads = 0
    tails = 0

    for j in tqdm(range((10000000)), desc=f'Game {game+1} Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
            
    print(f'Heads: {heads}, Tails: {tails}')       