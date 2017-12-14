import matplotlib.pyplot as plt
import pandas as pd

f = open('retrain_v2.txt', 'r')
retrain = f.readlines()
f.close()

r = []

for x in retrain:
	if retrain.index(x) % 6 == 2:
		y = x.split(' ')
		r.append((y[0], y[1]))

df = pd.DataFrame(r, columns = ['animal', 'score'])
df[['score']] = df[['score']].apply(pd.to_numeric)


plot = df.plot(kind = 'density', title = 'accuracy of inception_v3', legend = False, xlim = (0,1.0))
plot.set_xlabel('accuracy')
plot.set_ylabel('frequency')
plot_2 = df.plot(kind = 'hist', title = 'accuracy of inception_v3', legend = False, xlim = (0,1.0))
plot_2.set_xlabel('accuracy')
plot_2.set_ylabel('frequency')
plt.show()