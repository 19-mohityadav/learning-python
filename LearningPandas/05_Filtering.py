import pandas as pd

# Filtering --> Keeping the rows that match a condition

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

tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)
'''
      No        Name    Type1    Type2  Height  Weight  Legendary
2      3    Venusaur    Grass   Poison     2.0   100.0          0
22    23       Ekans   Poison      NaN     2.0     6.9          0
23    24       Arbok   Poison      NaN     3.5    65.0          0
94    95        Onix     Rock   Ground     8.8   210.0          0
102  103   Exeggutor    Grass  Psychic     2.0   120.0          0
114  115  Kangaskhan   Normal      NaN     2.2    80.0          0
129  130    Gyarados    Water   Flying     6.5   235.0          0
130  131      Lapras    Water      Ice     2.5   220.0          0
142  143     Snorlax   Normal      NaN     2.1   460.0          0
145  146     Moltres     Fire   Flying     2.0    60.0          1
147  148   Dragonair   Dragon      NaN     4.0    16.5          0
148  149   Dragonite   Dragon   Flying     2.2   210.0          0
149  150      Mewtwo  Psychic      NaN     2.0   122.0          1
'''

heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)
'''
      No       Name     Type1    Type2  Height  Weight  Legendary
2      3   Venusaur     Grass   Poison     2.0   100.0          0
58    59   Arcanine      Fire      NaN     1.9   155.0          0
67    68    Machamp  Fighting      NaN     1.6   130.0          0
74    75   Graveler      Rock   Ground     1.0   105.0          0
75    76      Golem      Rock   Ground     1.4   300.0          0
86    87    Dewgong     Water      Ice     1.7   120.0          0
90    91   Cloyster     Water      Ice     1.5   132.5          0
94    95       Onix      Rock   Ground     8.8   210.0          0
102  103  Exeggutor     Grass  Psychic     2.0   120.0          0
110  111    Rhyhorn    Ground     Rock     1.0   115.0          0
111  112     Rhydon    Ground     Rock     1.9   120.0          0
129  130   Gyarados     Water   Flying     6.5   235.0          0
130  131     Lapras     Water      Ice     2.5   220.0          0
142  143    Snorlax    Normal      NaN     2.1   460.0          0
148  149  Dragonite    Dragon   Flying     2.2   210.0          0
149  150     Mewtwo   Psychic      NaN     2.0   122.0          1
'''

legendary_pokemon = df[df["Legendary"] == 1]
# print(legendary_pokemon)
'''
      No      Name     Type1   Type2  Height  Weight  Legendary
143  144  Articuno       Ice  Flying     1.7    55.4          1
144  145    Zapdos  Electric  Flying     1.6    52.6          1
145  146   Moltres      Fire  Flying     2.0    60.0          1
149  150    Mewtwo   Psychic     NaN     2.0   122.0          1
'''

water_pokemon = df[df["Type1"] >= "Water"]
# print(water_pokemon)
'''
      No        Name  Type1     Type2  Height  Weight  Legendary
6      7    Squirtle  Water       NaN     0.5     9.0          0
7      8   Wartortle  Water       NaN     1.0    22.5          0
8      9   Blastoise  Water       NaN     1.6    85.5          0
53    54     Psyduck  Water       NaN     0.8    19.6          0
54    55     Golduck  Water       NaN     1.7    76.6          0
59    60     Poliwag  Water       NaN     0.6    12.4          0
60    61   Poliwhirl  Water       NaN     1.0    20.0          0
61    62   Poliwrath  Water  Fighting     1.3    54.0          0
71    72   Tentacool  Water    Poison     0.9    45.5          0
72    73  Tentacruel  Water    Poison     1.6    55.0          0
78    79    Slowpoke  Water   Psychic     1.2    36.0          0
79    80     Slowbro  Water   Psychic     1.6    78.5          0
85    86        Seel  Water       NaN     1.1    90.0          0
86    87     Dewgong  Water       Ice     1.7   120.0          0
89    90    Shellder  Water       NaN     0.3     4.0          0
90    91    Cloyster  Water       Ice     1.5   132.5          0
97    98      Krabby  Water       NaN     0.4     6.5          0
98    99     Kingler  Water       NaN     1.3    60.0          0
115  116      Horsea  Water       NaN     0.4     8.0          0
116  117      Seadra  Water       NaN     1.2    25.0          0
117  118     Goldeen  Water       NaN     0.6    15.0          0
118  119     Seaking  Water       NaN     1.3    39.0          0
119  120      Staryu  Water       NaN     0.8    34.5          0
120  121     Starmie  Water   Psychic     1.1    80.0          0
128  129    Magikarp  Water       NaN     0.9    10.0          0
129  130    Gyarados  Water    Flying     6.5   235.0          0
130  131      Lapras  Water       Ice     2.5   220.0          0
133  134    Vaporeon  Water       NaN     1.0    29.0          0
'''

pure_water_pokemon = df[(df["Type1"] >= "Water") | (df["Type2"] == "Water")] # | -> C style or , or -> .py style or
# print(pure_water_pokemon)
'''
      No        Name  Type1     Type2  Height  Weight  Legendary
6      7    Squirtle  Water       NaN     0.5     9.0          0
7      8   Wartortle  Water       NaN     1.0    22.5          0
8      9   Blastoise  Water       NaN     1.6    85.5          0
53    54     Psyduck  Water       NaN     0.8    19.6          0
54    55     Golduck  Water       NaN     1.7    76.6          0
59    60     Poliwag  Water       NaN     0.6    12.4          0
60    61   Poliwhirl  Water       NaN     1.0    20.0          0
61    62   Poliwrath  Water  Fighting     1.3    54.0          0
71    72   Tentacool  Water    Poison     0.9    45.5          0
72    73  Tentacruel  Water    Poison     1.6    55.0          0
78    79    Slowpoke  Water   Psychic     1.2    36.0          0
79    80     Slowbro  Water   Psychic     1.6    78.5          0
85    86        Seel  Water       NaN     1.1    90.0          0
86    87     Dewgong  Water       Ice     1.7   120.0          0
89    90    Shellder  Water       NaN     0.3     4.0          0
90    91    Cloyster  Water       Ice     1.5   132.5          0
97    98      Krabby  Water       NaN     0.4     6.5          0
98    99     Kingler  Water       NaN     1.3    60.0          0
115  116      Horsea  Water       NaN     0.4     8.0          0
116  117      Seadra  Water       NaN     1.2    25.0          0
117  118     Goldeen  Water       NaN     0.6    15.0          0
118  119     Seaking  Water       NaN     1.3    39.0          0
119  120      Staryu  Water       NaN     0.8    34.5          0
120  121     Starmie  Water   Psychic     1.1    80.0          0
128  129    Magikarp  Water       NaN     0.9    10.0          0
129  130    Gyarados  Water    Flying     6.5   235.0          0
130  131      Lapras  Water       Ice     2.5   220.0          0
133  134    Vaporeon  Water       NaN     1.0    29.0          0
137  138     Omanyte   Rock     Water     0.4     7.5          0
138  139     Omastar   Rock     Water     1.0    35.0          0
139  140      Kabuto   Rock     Water     0.5    11.5          0
140  141    Kabutops   Rock     Water     1.3    40.5          0
'''


