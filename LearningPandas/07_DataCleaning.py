import pandas as pd

# Data Cleaning --> The process of fixing / removing incomplete,
#                   incorrect or irrelevant data.
# about 75% of work with pandas is data cleaning

df = pd.read_csv("pokemon.csv")

# print(df.head())
'''
   No        Name  Type1   Type2  Height  Weight  Legendary
0   1   Bulbasaur  Grass  Poison     0.7     6.9          0
1   2     Ivysaur  Grass  Poison     1.0    13.0          0
2   3    Venusaur  Grass  Poison     2.0   100.0          0
3   4  Charmander   Fire     NaN     0.6     8.5          0
4   5  Charmeleon   Fire     NaN     1.1    19.0          0
'''

# 1. Drop irrelevant columns
df = df.drop(columns=["Legendary"])
# print(df)
'''
      No        Name    Type1   Type2  Height  Weight
0      1   Bulbasaur    Grass  Poison     0.7     6.9
1      2     Ivysaur    Grass  Poison     1.0    13.0
2      3    Venusaur    Grass  Poison     2.0   100.0
3      4  Charmander     Fire     NaN     0.6     8.5
4      5  Charmeleon     Fire     NaN     1.1    19.0
..   ...         ...      ...     ...     ...     ...
145  146     Moltres     Fire  Flying     2.0    60.0
146  147     Dratini   Dragon     NaN     1.8     3.3
147  148   Dragonair   Dragon     NaN     4.0    16.5
148  149   Dragonite   Dragon  Flying     2.2   210.0
149  150      Mewtwo  Psychic     NaN     2.0   122.0

[150 rows x 6 columns]
'''
df = df.drop(columns=["No"])
# print(df)
'''
           Name    Type1   Type2  Height  Weight
0     Bulbasaur    Grass  Poison     0.7     6.9
1       Ivysaur    Grass  Poison     1.0    13.0
2      Venusaur    Grass  Poison     2.0   100.0
3    Charmander     Fire     NaN     0.6     8.5
4    Charmeleon     Fire     NaN     1.1    19.0
..          ...      ...     ...     ...     ...
145     Moltres     Fire  Flying     2.0    60.0
146     Dratini   Dragon     NaN     1.8     3.3
147   Dragonair   Dragon     NaN     4.0    16.5
148   Dragonite   Dragon  Flying     2.2   210.0
149      Mewtwo  Psychic     NaN     2.0   122.0

[150 rows x 5 columns]
'''

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
# print(df)
'''
           Name     Type1   Type2  Height  Weight
0     Bulbasaur     Grass  Poison     0.7     6.9
1       Ivysaur     Grass  Poison     1.0    13.0
2      Venusaur     Grass  Poison     2.0   100.0
5     Charizard      Fire  Flying     1.7    90.5
11   Butterfree       Bug  Flying     1.1    32.0
..          ...       ...     ...     ...     ...
141  Aerodactyl      Rock  Flying     1.8    59.0
143    Articuno       Ice  Flying     1.7    55.4
144      Zapdos  Electric  Flying     1.6    52.6
145     Moltres      Fire  Flying     2.0    60.0
148   Dragonite    Dragon  Flying     2.2   210.0

[67 rows x 5 columns]
'''

df = df.fillna({"Type2": "None"})
# print(df)
'''
           Name    Type1   Type2  Height  Weight
0     Bulbasaur    Grass  Poison     0.7     6.9
1       Ivysaur    Grass  Poison     1.0    13.0
2      Venusaur    Grass  Poison     2.0   100.0
3    Charmander     Fire    None     0.6     8.5
4    Charmeleon     Fire    None     1.1    19.0
..          ...      ...     ...     ...     ...
145     Moltres     Fire  Flying     2.0    60.0
146     Dratini   Dragon    None     1.8     3.3
147   Dragonair   Dragon    None     4.0    16.5
148   Dragonite   Dragon  Flying     2.2   210.0
149      Mewtwo  Psychic    None     2.0   122.0

[150 rows x 5 columns]
'''

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"})
# print(df)
'''
           Name    Type1   Type2  Height  Weight
0     Bulbasaur    GRASS  Poison     0.7     6.9
1       Ivysaur    GRASS  Poison     1.0    13.0
2      Venusaur    GRASS  Poison     2.0   100.0
3    Charmander     FIRE    None     0.6     8.5
4    Charmeleon     FIRE    None     1.1    19.0
..          ...      ...     ...     ...     ...
145     Moltres     FIRE  Flying     2.0    60.0
146     Dratini   Dragon    None     1.8     3.3
147   Dragonair   Dragon    None     4.0    16.5
148   Dragonite   Dragon  Flying     2.2   210.0
149      Mewtwo  Psychic    None     2.0   122.0

[150 rows x 5 columns]
'''

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# print(df)
'''
           Name    Type1   Type2  Height  Weight
0     bulbasaur    GRASS  Poison     0.7     6.9
1       ivysaur    GRASS  Poison     1.0    13.0
2      venusaur    GRASS  Poison     2.0   100.0
3    charmander     FIRE    None     0.6     8.5
4    charmeleon     FIRE    None     1.1    19.0
..          ...      ...     ...     ...     ...
145     moltres     FIRE  Flying     2.0    60.0
146     dratini   Dragon    None     1.8     3.3
147   dragonair   Dragon    None     4.0    16.5
148   dragonite   Dragon  Flying     2.2   210.0
149      mewtwo  Psychic    None     2.0   122.0

[150 rows x 5 columns]
'''
# 5. Fixing Data types
df["Weight"] = df["Weight"].astype(int)

# print(df["Weight"])
'''
0        6
1       13
2      100
3        8
4       19
      ... 
145     60
146      3
147     16
148    210
149    122
Name: Weight, Length: 150, dtype: int64
'''

# 6. Removing duplicate entries
df = df.drop_duplicates()

# print(df)

'''
           Name    Type1   Type2  Height  Weight
0     bulbasaur    GRASS  Poison     0.7       6
1       ivysaur    GRASS  Poison     1.0      13
2      venusaur    GRASS  Poison     2.0     100
3    charmander     FIRE    None     0.6       8
4    charmeleon     FIRE    None     1.1      19
..          ...      ...     ...     ...     ...
145     moltres     FIRE  Flying     2.0      60
146     dratini   Dragon    None     1.8       3
147   dragonair   Dragon    None     4.0      16
148   dragonite   Dragon  Flying     2.2     210
149      mewtwo  Psychic    None     2.0     122

[150 rows x 5 columns]
'''