import pandas as pd

df = pd.read_csv("pokemon.csv") # for JSON use read_json(
# print(df)
'''
      No        Name    Type1   Type2  Height  Weight  Legendary
0      1   Bulbasaur    Grass  Poison     0.7     6.9          0
1      2     Ivysaur    Grass  Poison     1.0    13.0          0
2      3    Venusaur    Grass  Poison     2.0   100.0          0
3      4  Charmander     Fire     NaN     0.6     8.5          0
4      5  Charmeleon     Fire     NaN     1.1    19.0          0
..   ...         ...      ...     ...     ...     ...        ...
145  146     Moltres     Fire  Flying     2.0    60.0          1
146  147     Dratini   Dragon     NaN     1.8     3.3          0
147  148   Dragonair   Dragon     NaN     4.0    16.5          0
148  149   Dragonite   Dragon  Flying     2.2   210.0          0
149  150      Mewtwo  Psychic     NaN     2.0   122.0          1

[150 rows x 7 columns]
'''
print(df.to_string()) # to display all the data in file
