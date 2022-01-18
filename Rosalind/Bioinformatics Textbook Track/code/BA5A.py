# Find the Minimum Number of Coins Needed to Make Change
# https://rosalind.info/problems/ba5a/

from utilities import get_file, get_answer_file

def dp_change(change, coin_array):
    num_array = [0] + [10**5] * change
    
    for coin in coin_array:
    	for price in range(coin, change + 1):
            if price >= coin:
                num_array[price] = min(num_array[price], num_array[price - coin] + 1)
    
    return num_array[change]

def greedy_change(change, coin_array):
    num = 0
    for coin in reversed(coin_array):
        num += change // coin
        change = change % coin
    return num

def recursive_change(change, coin_array):
    if change == 0:
        return 0
    min_coin = 10**9
    for coin in reversed(coin_array):
        if change >= coin:
            num_coin = recursive_change(change - coin, coin_array)
            if num_coin + 1 < min_coin:
                min_coin = num_coin + 1
    return min_coin

with get_file() as file:
    change = int(file.readline().rstrip())
    coin_array = list(map(int, file.readline().split(",")))

with get_answer_file() as file:
    print(dp_change(change, coin_array), file=file)
    print(greedy_change(change, coin_array))
    # print(recursive_change(change, coin_array))
    # The recursive_change fuction doesn't work.
    # Maximum recursion depth exceeded while calling a Python object.
    # If you want to use the recursive_chage function, you should change recursive limit by using line of code as "sys.setrecursionlimit(150000)".