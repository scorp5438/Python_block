import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

data.loc[data['whoAmI'] == 'robot', 'robot'] = (data['whoAmI'] == 'robot') * 1
data.loc[data['whoAmI'] == 'human', 'human'] = (data['whoAmI'] == 'human') * 1

data = data.convert_dtypes(int)

print(data[['robot', 'human']].fillna(0))




