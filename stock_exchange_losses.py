"""
A finance company is carrying out a study on the
worst stock investments and would like to acquire a program
to do so. The program must be able to analyze a chronological
series of stock values in order to show the largest loss that
it is possible to make by buying a share at a given time t0
and by selling it at a later date t1. The loss will be expressed
as the difference in value between t0 and t1. If there is no loss,
the loss will be worth 0.

https://www.codingame.com/ide/puzzle/stock-exchange-losses
"""

number_of_stocks = int(input())
stock_values = list(map(int, input().split()))

highest_stock = stock_values[0]
highest_loss = 0

for stock_value in stock_values:
  if highest_stock - stock_value > highest_loss:
    highest_loss = highest_stock - stock_value
  if highest_stock < stock_value:
    highest_stock = stock_value
print(-highest_loss)