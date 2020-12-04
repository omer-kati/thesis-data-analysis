import pandas as pd
from scipy.stats import f_oneway

data = pd.read_csv('data_participants')


mf = data['Q4'][2:].values.tolist()

print('male', mf.count('1'))
print('female', mf.count('2'))

a = data['Q6'][2:].values
ta = []

for i in a:
    ta.append(int(i))

print('min age', min(ta))
print('max age', min(ta))
print('avg age', sum(ta) / len(ta))

droplist = ['Q2', 'Q4', 'Q6', 'Q16_1',
            'Q16_2', 'Q16_3', 'Q41_1', 'Q41_2', 'Q41_3', 'SC0']

data = data.drop(columns=droplist)
rank1 = []
rank2 = []
rank3 = []

for column in data.columns:

    if int(column[-1]) == 1:
        for i in data[column][2:]:
            rank1.append(int(i))
    elif int(column[-1]) == 2:
        for i in data[column][2:]:
            rank2.append(int(i))

    elif int(column[-1]) == 3:
        for i in data[column][2:]:
            rank3.append(int(i))

model1 = [1] * rank1.count(1) + [2] * rank2.count(1) + [3] * rank3.count(1)
model2 = [1] * rank1.count(2) + [2] * rank2.count(2) + [3] * rank3.count(2)
model3 = [1] * rank1.count(3) + [2] * rank2.count(3) + [3] * rank3.count(3)

results = pd.DataFrame()

results['model1'] = model1
results['model2'] = model2
results['model3'] = model3

print(results.describe())
print(f_oneway(model1, model2, model3))
