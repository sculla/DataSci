import numpy as np
import pandas as pd

sal = pd.DataFrame(pd.read_csv('Salaries.csv'))
print('\n')
print(sal['BasePay'].mean())
print('\n')
print(sal['OvertimePay'].max())
print('\n')
print(sal[sal['EmployeeName'] == "JOSEPH DRISCOLL"]['JobTitle'])
print('\n')
print(sal[sal['EmployeeName'] == "JOSEPH DRISCOLL"]['TotalPayBenefits'])
print('\n')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
print('\n')
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])
print('\n')
print(sal.groupby('Year').mean()['BasePay'])
print('\n')
print(sal['JobTitle'].nunique())
print('\n')
print(sal['JobTitle'].value_counts().head(5))
print('\n')
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))
print('\n')
print(sum(sal['JobTitle'].apply(lambda x: 'chief' in x.lower())))
print('\n')
sal['title_len'] = sal['JobTitle'].apply(lambda x : len(x))
print(sal[['title_len','TotalPayBenefits']].corr())



# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 148654 entries, 0 to 148653
# Data columns (total 13 columns):
# Id                  148654 non-null int64
# EmployeeName        148654 non-null object
# JobTitle            148654 non-null object
# BasePay             148045 non-null float64
# OvertimePay         148650 non-null float64
# OtherPay            148650 non-null float64
# Benefits            112491 non-null float64
# TotalPay            148654 non-null float64
# TotalPayBenefits    148654 non-null float64
# Year                148654 non-null int64
# Notes               0 non-null float64
# Agency              148654 non-null object
# Status              0 non-null float64
# dtypes: float64(8), int64(2), object(3)
# memory usage: 14.7+ MB