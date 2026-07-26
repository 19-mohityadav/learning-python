from operator import index

import pandas as pd

# DataFrame -> A tabular data structure with rows and columns.(2 D)
#              Similar to an Excel spreadsheet or Google sheets

data = {"Name": ["Oggy", "Jack", "Cockroaches"],
        "Age": [25, 35, 45],
        }

df = pd.DataFrame(data, index=['Character 1', 'Character 2', 'Character 3'])
# print(df)
'''
                    Name  Age
Character 1         Oggy   25
Character 2         Jack   35
Character 3  Cockroaches   45
'''
# print(df.loc['Character 1'])
'''
Name    Oggy
Age       25
Name: Character 1, dtype: object
'''

# Add a new column
df["Job"] = ["House Wife", "Military Man", "Naughty Children"]
# print(df)
'''
                    Name  Age               Job
Character 1         Oggy   25        House Wife
Character 2         Jack   35      Military Man
Character 3  Cockroaches   45  Naughty Children
'''

# Add a new row
new_row = pd.DataFrame([{"Name": "Olivia",
                         "Age": 25,
                         "Job": "Neighbour",
                         }],
                       index=["Character 4"]
                       )
df = pd.concat([df, new_row]) # This adding is done by making new DF and Concatenating with prev
# print(df)
'''
                   Name  Age               Job
Character 1         Oggy   25        House Wife
Character 2         Jack   35      Military Man
Character 3  Cockroaches   45  Naughty Children
Character 4       Olivia   25         Neighbour
'''

# Add new rows
new_rows = pd.DataFrame([{"Name": "Bheem", "Age": 15, "Job": "Laddo Khana"},
                         {"Name": "Kaliya", "Age": 20, "Job": "Bully"}],
                        index= ['Character 5', "Character 6"]
                        )
df = pd.concat([df, new_rows])
print(df)
'''
                    Name  Age               Job
Character 1         Oggy   25        House Wife
Character 2         Jack   35      Military Man
Character 3  Cockroaches   45  Naughty Children
Character 4       Olivia   25         Neighbour
Character 5        Bheem   15       Laddo Khana
Character 6       Kaliya   20             Bully
'''