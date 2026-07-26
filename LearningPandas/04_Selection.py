import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")
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

# Selection by Column

# print(df["Name"])
'''
0       Bulbasaur
1         Ivysaur
2        Venusaur
3      Charmander
4      Charmeleon
          ...    
145       Moltres
146       Dratini
147     Dragonair
148     Dragonite
149        Mewtwo
Name: Name, Length: 150, dtype: str
'''

# print(df[['Name', 'Height']])
'''
           Name  Height
0     Bulbasaur     0.7
1       Ivysaur     1.0
2      Venusaur     2.0
3    Charmander     0.6
4    Charmeleon     1.1
..          ...     ...
145     Moltres     2.0
146     Dratini     1.8
147   Dragonair     4.0
148   Dragonite     2.2
149      Mewtwo     2.0

[150 rows x 2 columns]
'''

# Selection by rows
# print(df.loc[0])
'''
No                   1
Name         Bulbasaur
Type1            Grass
Type2           Poison
Height             0.7
Weight             6.9
Legendary            0
Name: 0, dtype: object
'''

# After index_col ="Name"
# print(df.loc['Pikachu'])
'''
No                 25
Type1        Electric
Type2             NaN
Height            0.4
Weight            6.0
Legendary           0
Name: Pikachu, dtype: object
'''
# print(df.loc["Charizard", ["Height", "Weight", "Legendary"]])
'''
Height        1.7
Weight       90.5
Legendary     0.0
Name: Charizard, dtype: float64
'''

# print(df.iloc[0:11])
'''
            No  Type1   Type2  Height  Weight  Legendary
Name                                                    
Bulbasaur    1  Grass  Poison     0.7     6.9          0
Ivysaur      2  Grass  Poison     1.0    13.0          0
Venusaur     3  Grass  Poison     2.0   100.0          0
Charmander   4   Fire     NaN     0.6     8.5          0
Charmeleon   5   Fire     NaN     1.1    19.0          0
Charizard    6   Fire  Flying     1.7    90.5          0
Squirtle     7  Water     NaN     0.5     9.0          0
Wartortle    8  Water     NaN     1.0    22.5          0
Blastoise    9  Water     NaN     1.6    85.5          0
Caterpie    10    Bug     NaN     0.3     2.9          0
Metapod     11    Bug     NaN     0.7     9.9          0
'''

# print(df.iloc[0:11:2, 0:3])
'''
            No  Type1   Type2
Name                         
Bulbasaur    1  Grass  Poison
Venusaur     3  Grass  Poison
Charmeleon   5   Fire     NaN
Squirtle     7  Water     NaN
Blastoise    9  Water     NaN
Metapod     11    Bug     NaN
'''

# Exercise

pokemon = input("Enter pokemon name: ")

try:
    print(df.loc[pokemon])
except:
    print(f"{pokemon} not found!")


