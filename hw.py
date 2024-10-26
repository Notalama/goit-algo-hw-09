def find_coins_greedy(amount):

  coins = {50: 0, 25: 0, 10: 0, 5: 0, 2: 0, 1: 0}
  denominations = list(coins.keys())
  remaining = amount

  for coin in denominations:
    while remaining >= coin:
      coins[coin] += 1
      remaining -= coin

  return coins


def find_min_coins(amount):

  coins = [1, 2, 5, 10, 25, 50]
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0
  used_coins = [[] for _ in range(amount + 1)]

  for i in range(1, amount + 1):
    for coin in coins:
      if i >= coin and dp[i - coin] + 1 < dp[i]:
        dp[i] = dp[i - coin] + 1
        used_coins[i] = used_coins[i - coin] + [coin]

  result = {coin: 0 for coin in coins}
  for coin in used_coins[amount]:
    result[coin] += 1

  return result


amount = 113
greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

print(f"Жадібний алгоритм: {greedy_result}")
print(f"Динамічне програмування: {dp_result}")
