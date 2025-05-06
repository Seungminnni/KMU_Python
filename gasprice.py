f = open("gas_prices.txt")
contents = f.read()
tokens = constents.split()
# avg_price_bel = 0

for i in range(0, len(tokens), 3):
   sum_price