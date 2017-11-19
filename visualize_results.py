from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import re

f = open('results.txt', 'r')
results = f.read()
results = results.split('???')
f.close()

top_scores = []


for x in results[:-1]:
	temp = re.findall('(.+)\s\(.*(0\.\d+)', x)[0]
	top_scores.append(temp)

df = pd.DataFrame(top_scores, columns = ['animal', 'score'])
df[['score']] = df[['score']].apply(pd.to_numeric)


plot = df.plot(kind = 'density', title = 'accuracy of inception_v3', legend = False, xlim = (0,1.0))
plot.set_xlabel('accuracy')
plot.set_ylabel('frequency')

#plt.savefig('density.jpg')

plot_2 = df.plot(kind = 'hist', title = 'accuracy of inception_v3', legend = False, xlim = (0,1.0))
plot_2.set_xlabel('accuracy')
plot_2.set_ylabel('frequency')

#plt.savefig('histogram.jpg')

f = open('incorrect_analysis.txt')
results = f.read()
f.close()

pairs = []

temp = re.findall('.*[\d]+\)\s.*\s', results)
for x in temp:
	pair = x.split('\n')[:2]
	pair[0] = pair[0].split(' (')[0]
	pairs.append((pair[1], pair[0]))

df = pd.DataFrame(pairs, columns = ['class', 'incorrect_class'])

df.groupby(df['class']).count().plot(kind = 'bar', title = 'incorrect classifications by animal', legend = False)
#plt.savefig('incorrect_classes.jpg')

wild = df[df['class'] == 'wildebeest']
incorrect = wild.groupby(['incorrect_class']).count().plot(kind = 'bar', title = 'incorrect classifications')

rhino = df[df['class'] == 'rhinoceros']
rhino.groupby(['incorrect_class']).count().plot(kind = 'bar', ax = incorrect, color = 'red')

incorrect.legend(labels = ['wildebeest', 'rhinoceros'])
plt.tight_layout()
plt.savefig('incorrect_classes_stacked_3.jpg')
