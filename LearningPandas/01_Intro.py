import pandas as pd

# print(pd.__version__) # version of pd

# Series --> In pandas it is a 1D labeled array that can hold any data type
#           Like single column in a spreadsheet i.e 1D

# creating series
data = [100, 102, 104]
series = pd.Series(data) # Series is a constructor not a fn
# print(series)
'''
0    100
1    102
2    104
dtype: int64 --> String -> Object
'''
series2 = pd.Series(data, index=["apartment #1", "apartment #2", "apartment #3"])
# print(series2)
'''
apartment #1    100
apartment #2    102
apartment #3    104
dtype: int64
'''

# To print or access the val by label
# print(series2.loc["apartment #1"]) # 100

# by integer position like accessing in array
# print(series2.iloc[0]) # 100


# Filter by value
data2 = [100, 102, 104, 200, 202, 204]
series3 = pd.Series(data2, index=["a", "b", "c", "d", "e", "f"])
# print(series3[series3 >= 200])
'''
d    200
e    202
f    204
dtype: int64
'''

# Daily requirement of calories
calories = {"Day 1": 1700, "Day 2": 2000, "Day 3": 2500, "Day 4": 3000}
series4 = pd.Series(calories)
print(series4.loc["Day 1"]) # 1700

series4.loc["Day 2"] += 200
print(series4.loc["Day 2"]) # 2200

# filtering by val
print(series4[series4 >= 2000])
'''
Day 2    2200
Day 3    2500
Day 4    3000
dtype: int64
'''