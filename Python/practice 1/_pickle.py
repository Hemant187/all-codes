import pickle
import requests
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = requests.get(url).text
# print(data)
l1 = data.split('\n')
# print(l1)
l2 = [item.split(',') for item in l1  if len(item)!=0 ]
# print(l2)
with open('mypkl.pkl','wb') as f:
    pickle.dump(l2,f)

with open('mypkl.pkl','rb') as op:
    print(pickle.load(op))