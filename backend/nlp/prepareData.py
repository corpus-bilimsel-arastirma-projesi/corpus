# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 06:31:49 2019

@author: asuer
"""
import pandas as pd
import re

uk =pd.read_json("UK_afterJaccard.json")
uk['country'] = 'uk'
cn=pd.read_json("CN_afterJaccard.json")
cn['country'] = 'cn'
us=pd.read_json("US_afterJaccard.json")
us['country'] = 'us'

df=pd.concat([us, uk, cn], ignore_index=True)
cols=['title', 'date', 'content', 'source','country']
df=df[cols]
df['date']=pd.to_datetime(df['date'])
de=pd.read_csv("dwCleaned.csv",  encoding='utf-8')
de['date'] = de['date'].replace('\n','', regex=True)
de.rename(columns={'Source': 'source'}, inplace=True)
de['country'] = 'de'
de['date'] = pd.to_datetime(de['date'])
df=pd.concat([df, de], ignore_index=True)

'''1.clean categoricals, source is an example, user should be able to
select the category and do the cleaning, burada value_counts ile sutunu kontrol edecek,
bu usera gozukecek, sonra, orada gordugune gore temizlik yapacak, '''
#see if anything not good
df['source']=df['source'].str.lower().str.strip()
df['source'].value_counts()

'''burada bir box olacak, soracak kulliniciya'''

def deleteBetween(startWord, endWord, dataframe):
    pattern = startWord + "(.*)" + endWord
    for j in range(len(dataframe)):
            dataframe[j] = re.sub(pattern,'',dataframe[j])
    return dataframe
'''
örnek kullanım:
sW='journal' #blogsdc
eW='abstracts'# bog
deleteBetween(sW, eW,df.iloc[0:, 3])
'''
def deleteWord(word,  dataframe):
    pattern = word
    for j in range(len(dataframe)):
            dataframe[j] = re.sub(pattern,'',dataframe[j])
    return dataframe

def deleteEnd(end,dataframe):
    pattern = r'[a-zA-Z0-9_.+-]+' + end
    for j in range(len(dataframe)):
        dataframe[j] = re.sub(pattern,"",dataframe[j])
    return dataframe

def deleteBeginning(start,dataframe):
    pattern =   start + r'[a-zA-Z0-9_.+-]+'
    for j in range(len(dataframe)):
        dataframe[j] = re.sub(pattern,"",dataframe[j])
    return dataframe


df['source']=df['source'].str.replace(' ', '', regex=True)

df["source"]=  pd.Categorical(df["source"])
df["source"]= df["source"].cat.remove_categories('')
df['source'].value_counts()



'''make a new year variable, or month variable, replace year by month,
burada date degiskeninden yil, ay ve gun uretip yeni bir column eklemeyi soracak'''
yr = []
for date in df['date']:
    xx=date.year
    yr.append(str(xx))
df.loc[:, 'year'] = yr


'''save'''
#df.to_json(r'ai_cntries.json')
