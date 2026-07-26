import pandas as pd

# Aggregate functions --> Reduces a set of values into a single summary value
#                         It is used to summarize and analyze data mostly eith groupby() Fn

df = pd.read_csv('pokemon.csv')

# print(df.head())
'''
   No        Name  Type1   Type2  Height  Weight  Legendary
0   1   Bulbasaur  Grass  Poison     0.7     6.9          0
1   2     Ivysaur  Grass  Poison     1.0    13.0          0
2   3    Venusaur  Grass  Poison     2.0   100.0          0
3   4  Charmander   Fire     NaN     0.6     8.5          0
4   5  Charmeleon   Fire     NaN     1.1    19.0          0
'''

# For whole DF

# print(df.mean(numeric_only=True))  #mean of all numeric val
'''
No           75.500000
Height        1.200000
Weight       46.231333
Legendary     0.026667
dtype: float64
'''

# print(df.sum(numeric_only=True))
'''
No           11325.0
Height         180.0
Weight        6934.7
Legendary        4.0
dtype: float64
'''

# print(df.min(numeric_only=True))
'''
No           1.0
Height       0.2
Weight       0.1
Legendary    0.0
dtype: float64
'''
# print(df.max(numeric_only=True))
'''
No           150.0
Height         8.8
Weight       460.0
Legendary      1.0
dtype: float64
'''
# print(df.count())
'''
No           150
Name         150
Type1        150
Type2         67
Height       150
Weight       150
Legendary    150
dtype: int64
'''

# For Single Column
# print(df["Height"].mean())  # 1.2
# print(df["Height"].sum()) #180.0
# print(df["Weight"].min()) # 0.1
# print(df["Weight"].max()) # 460.0
# print(df["Weight"].count()) # 150

# Grouping the DF

group = df.groupby('Type1')
# print(group)  # <pandas.api.typing.DataFrameGroupBy object at 0x0000021B02BD95B0>
# print(group["Height"].mean())
'''
Type1
Bug         0.900000
Dragon      2.666667
Electric    0.855556
Fairy       0.950000
Fighting    1.185714
Fire        1.216667
Ghost       1.466667
Grass       1.083333
Ground      0.850000
Ice         1.550000
Normal      0.986364
Poison      1.221429
Psychic     1.371429
Rock        1.844444
Water       1.300000
Name: Height, dtype: float64
'''
# print(df.groupby('Type1')['Height'].describe())
'''
          count      mean       std  min    25%   50%    75%  max
Type1                                                            
Bug        12.0  0.900000  0.463191  0.3  0.525  1.00  1.200  1.5
Dragon      3.0  2.666667  1.171893  1.8  2.000  2.20  3.100  4.0
Electric    9.0  0.855556  0.418662  0.3  0.500  0.80  1.100  1.6
Fairy       2.0  0.950000  0.494975  0.6  0.775  0.95  1.125  1.3
Fighting    7.0  1.185714  0.422013  0.5  0.900  1.40  1.500  1.6
Fire       12.0  1.216667  0.500606  0.6  0.850  1.10  1.700  2.0
Ghost       3.0  1.466667  0.152753  1.3  1.400  1.50  1.550  1.6
Grass      12.0  1.083333  0.545783  0.4  0.700  1.00  1.325  2.0
Ground      8.0  0.850000  0.518239  0.2  0.550  0.85  1.000  1.9
Ice         2.0  1.550000  0.212132  1.4  1.475  1.55  1.625  1.7
Normal     22.0  0.986364  0.584967  0.3  0.425  1.00  1.350  2.2
Poison     14.0  1.221429  0.790500  0.4  0.800  1.05  1.375  3.5
Psychic     7.0  1.371429  0.372891  0.9  1.150  1.30  1.550  2.0
Rock        9.0  1.844444  2.652410  0.4  0.500  1.00  1.400  8.8
Water      28.0  1.300000  1.131043  0.3  0.800  1.10  1.525  6.5
'''

