from matplotlib import pyplot as plt
import matplotlib.style as sty
import pandas as pd

df3 = pd.read_csv('df3')

df3.plot.scatter(x='a',y='b',figsize = (12,3),c='red', s=50)
plt.xlim(-.2,1.2)
plt.ylim(-.2,1.2)
plt.show()

df3['a'].plot.hist(edgecolor='black')
plt.show()

sty.use("ggplot")
df3['a'].plot.hist(bins=25,edgecolor='white', alpha=0.5)
plt.show()

df3[['a','b']].plot.box()
plt.show()

df3['d'].plot.kde()
plt.show()

df3['d'].plot.kde(lw=5,ls='--')
plt.show()

df3.ix[0:30].plot.area(alpha=0.4)
plt.show()

df3.head(30).plot.area(alpha=0.4)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


# RangeIndex: 500 entries, 0 to 499
# Data columns (total 4 columns):
# a    500 non-null float64
# b    500 non-null float64
# c    500 non-null float64
# d    500 non-null float64
# dtypes: float64(4)
# memory usage: 15.7 KB