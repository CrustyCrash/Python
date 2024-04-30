print("Enter quantity, cost of 1 unit is 100")
quant = int(input())
cost = 100 * quant

if cost > 1000:
    print("Final price after 10% discount is:", round(cost * 0.90, 2))
else:
    print("Final price is:", cost)
