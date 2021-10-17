prices = [51, 45.04, 60.1, 50, 49.40, 0.5, 0.05, 9.99, 10, 24.87, 100.01]
print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
prices.sort(reverse=True)
print(prices)
print(id(prices))
print(sorted(prices)[6::1])
print(id(prices))
prices = [str(price) for price in prices]
prices = [f"{''.join(price.split('.')[:1])} руб {''.join(price.split('.')[1:]):<02} коп" for price in prices]
print(prices)
print(id(prices))