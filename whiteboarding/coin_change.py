#!/usr/bin/python3
"""
Coin Change problem
"""
#need to be given the array of coins, the sum to find, the idx for the coin and the memo dict
def coin_change(sum, coins, coin_idx, memo):
    # check if the sum == 0
    if sum == 0:
        return 1

    # check if the sum < 0
    if sum < 0:
        return 0

    # if idx is greater then len of coins
    if coin_idx >= len(coins):
        return 0

    # create the key sum-idx
    key = "{}-{}".format(sum, coin_idx)

    # check if key in memo dict
    if memo.get(key, None) != None:
        # if found return the value stored in dict
        return memo[key]

    # return coinchange(next coin) + coinchange(subtract current coin from sum)
    return(coin_change(sum, coins, coin_idx + 1, memo) +
                       coin_change(sum - coins[coin_idx], coins, coin_idx, memo))

t_sum = 4
t_coins = [1, 2, 3]
t_coin_idx = 0
t_memo = {}
print("sum:{} coins:{} ways:{}".format(
    t_sum, t_coins, coin_change(t_sum, t_coins, t_coin_idx, t_memo)))


t_sum = 14
t_coins = [1, 5, 3]
t_coin_idx = 0
t_memo = {}
print("sum:{} coins:{} ways:{}".format(
    t_sum, t_coins, coin_change(t_sum, t_coins, t_coin_idx, t_memo)))


t_sum = 18
t_coins = [1, 5, 3, 9]
t_coin_idx = 0
t_memo = {}
print("sum:{} coins:{} ways:{}".format(
    t_sum, t_coins, coin_change(t_sum, t_coins, t_coin_idx, t_memo)))
