# import pandas as pd
# import random

# lst = ['robot'] * 10
# lst += ['human'] * 10

# random.shuffle(lst)

# data = pd.DataFrame({'whoAmI': lst})

# data.loc[data['whoAmI'] == 'robot', 'robot'] = (data['whoAmI'] == 'robot') * 1
# data.loc[data['whoAmI'] == 'human', 'human'] = (data['whoAmI'] == 'human') * 1

# data = data.convert_dtypes(int)

# print(data[['robot', 'human']].fillna(0))

# import random

# lst = ['robot'] * 10
# lst += ['human'] * 10

# random.shuffle(lst)

# print(f"№ {'robot':^7} {'human':^5}")
# for i in range(len(lst)):
#     if i < 9: print(f"{i+1} {int('robot' == lst[i]):^7} {int('human' == lst[i]):^5}")
#     elif i >= 9: print(f"{i+1} {int('robot' == lst[i]):^6} {int('human' == lst[i]):^5}")