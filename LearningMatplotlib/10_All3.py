import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("../LearningPandas./pokemon.csv")

# print(df.head())
'''
   No        Name  Type1   Type2  Height  Weight  Legendary
0   1   Bulbasaur  Grass  Poison     0.7     6.9          0
1   2     Ivysaur  Grass  Poison     1.0    13.0          0
2   3    Venusaur  Grass  Poison     2.0   100.0          0
3   4  Charmander   Fire     NaN     0.6     8.5          0
4   5  Charmeleon   Fire     NaN     1.1    19.0          0
'''

# print(df["Type1"])
# print(df["Type1"].value_counts())

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index,type_count)

plt.title("Type 1 Pokemeon")
plt.xlabel("Counts")
plt.ylabel("Pokemeon")
plt.tight_layout()

plt.show()