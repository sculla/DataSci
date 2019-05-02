import numpy as np
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,iplot
import cufflinks as cf
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4),columns="A B C D".split())
df.head()

df2 = pd.DataFrame({'Category':"A B C".split(),'Values':[32,43,50]})

