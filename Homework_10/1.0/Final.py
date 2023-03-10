# Урок 10. Построение графиков
# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
import pandas as pd
import random 
lst = ['robot']*10
lst += ['human']*10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})
print(df['whoAmI'])
def onehot_maker(type):
    if type == 'robot':
        return 0 
    else: 
        return 1
 
df['whoAmI'] = df['whoAmI'].apply(onehot_maker)
print(df['whoAmI'])
