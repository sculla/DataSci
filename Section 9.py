import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats as sta
import numpy as np
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

graph = sns.jointplot('fare','age',titanic,xlim=(-100,600),ylim=(-10,90))
graph.annotate(sta.pearsonr)
plt.show()


sns.distplot(titanic['fare'],kde=False,color='r',bins=36)
plt.ylim(top=500)
plt.xlim(left=0,xmax=600)

plt.show()


sns.boxplot(x='class',y='age',data=titanic)
plt.ylim(0,80)
plt.show()

sns.swarmplot(x='class',y='age',data=titanic)
plt.ylim(-10,90)
plt.show()


sns.countplot(x='sex',data=titanic)
plt.ylim(0,600)
plt.show()

sns.heatmap(titanic.corr(),cmap='coolwarm',)
plt.show()

g = sns.FacetGrid(titanic,col='sex')
plt.xlim(0,80)
plt.ylim(0,120)
g.map(plt.hist,'age',bins=10)
plt.xticks(np.arange(0,81,10))
plt.yticks(np.arange(0,121,20))
plt.show()

# titanic.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 15 columns):
# survived       891 non-null int64
# pclass         891 non-null int64
# sex            891 non-null object
# age            714 non-null float64
# sibsp          891 non-null int64
# parch          891 non-null int64
# fare           891 non-null float64
# embarked       889 non-null object
# class          891 non-null category
# who            891 non-null object
# adult_male     891 non-null bool
# deck           203 non-null category
# embark_town    889 non-null object
# alive          891 non-null object
# alone          891 non-null bool
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)
# memory usage: 80.6+ KB