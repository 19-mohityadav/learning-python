# default arguments --> A default value for certain parameters
#                       default is used when that argument is omitted
#                       make your function more flexible, reduce # of arguments
#                       1. positional , 2. Default , 3. Keyword , 4. arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)
#
# print(net_price(500, 0, 20))
# print(net_price(100))

import time

def count(end, start = 0):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("DONE")

count(5)
count(15, 10)


