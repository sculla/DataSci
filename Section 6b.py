import numpy as np
import pandas as pd

df = pd.DataFrame(pd.read_csv('Ecommerce Purchases'))

print(df['Purchase Price'].mean())

print(df['Purchase Price'].max())

print(df['Purchase Price'].min())

print(df['Language'].value_counts()['en'])

print(df['Job'].value_counts()['Lawyer'])

print(df['AM or PM'].value_counts())

print(df['Job'].value_counts().head(5))

print(df[df['Lot'] == '90 WT']['Purchase Price'])

print(df[df['Credit Card'] == 4926535242672853]['Email'])

print(df[(df['CC Provider'] == 'American Express') &
         (df['Purchase Price'] > 95)]['IP Address'].count())

print(df['CC Exp Date'].apply(lambda x: x[-2:]).value_counts()['25'])

print(df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10000 entries, 0 to 9999
# Data columns (total 14 columns):
# Address             10000 non-null object
# Lot                 10000 non-null object
# AM or PM            10000 non-null object
# Browser Info        10000 non-null object
# Company             10000 non-null object
# Credit Card         10000 non-null int64
# CC Exp Date         10000 non-null object
# CC Security Code    10000 non-null int64
# CC Provider         10000 non-null object
# Email               10000 non-null object
# Job                 10000 non-null object
# IP Address          10000 non-null object
# Language            10000 non-null object
# Purchase Price      10000 non-null float64
# dtypes: float64(1), int64(2), object(11)
# memory usage: 1.1+ MB
