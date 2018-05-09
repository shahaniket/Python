# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:09:37 2018

@author: aniketsha
"""
import pandas as pd

dataset = pd.read_csv('Ecommerce Purchases')

# number of columns and rows
print (len(dataset.columns))
print (len(dataset.index))
print (dataset.info())
'''
Data columns (total 14 columns):
Address             10000 non-null object
Lot                 10000 non-null object
AM or PM            10000 non-null object
Browser Info        10000 non-null object
Company             10000 non-null object
Credit Card         10000 non-null int64
CC Exp Date         10000 non-null object
CC Security Code    10000 non-null int64
CC Provider         10000 non-null object
Email               10000 non-null object
Job                 10000 non-null object
IP Address          10000 non-null object
Language            10000 non-null object
Purchase Price      10000 non-null float64
'''

# What is the average Purchase Price?
print (dataset['Purchase Price'].mean()) 
## 50.34730200000025

# What were the highest and lowest purchase prices?
print (dataset['Purchase Price'].max())
## 99.99
print (dataset['Purchase Price'].min())
## 0.0

# How many people have English 'en' as their Language of choice on the website?
print (len(dataset[dataset['Language']=='en']))
## 1098

# How many people have the job title of "Lawyer" ?
print (len(dataset[dataset['Job']=='Lawyer']))
## 30

# How many people made the purchase during the AM and how many people made the purchase during PM ?
print ([dataset['AM or PM'].value_counts()])
'''
PM    5068
AM    4932
'''


# What are the 5 most common Job Titles?
print (dataset['Job'].value_counts().head(5))
'''
Interior and spatial designer    31
Lawyer                           30
Social researcher                28
Purchasing manager               27
Designer, jewellery              27
'''
# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print (dataset[dataset['Lot']=='90 WT']['Purchase Price'])
## 513    75.1

# What is the email of the person with the following Credit Card Number: 4926535242672853
print (dataset[dataset['Credit Card']==4926535242672853]['Email'])
## 1234    bondellen@williams-garza.com

# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print (sum(dataset[dataset['CC Provider']=='American Express']['Purchase Price'] > 95))
## 39

# Hard: How many people have a credit card that expires in 2025? 
print ([x.split('/')[1] for x in dataset['CC Exp Date']].count('25'))
## 1033

# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print (dataset['Email'].apply(lambda x:x.split('@')[1]).value_counts().head(5))