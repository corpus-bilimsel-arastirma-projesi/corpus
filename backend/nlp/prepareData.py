# -*- coding: utf-8 -*-
import pandas as pd
import re

#dosyayı alıp dataframe'e cevirmek icin.
def getFile(file):
    dataFrame = pd.read_json(file) #simdilik json, degisebilir
    return dataFrame

#birden fazla dosyayı birlestirip kullanmak isterse
def fileConcat(fileList):
    dataFrame = pd.concat(fileList,ignore_index=True)
    return dataFrame

#dataframe'in columnlarını(content,source vs.) liste olarak verir
def listColumn(dataframe):
    return list(dataframe.columns)

#düzelt ekleme yap, sadece yıl icin, ay ve günü ekle
def chooseDate(dateVar,dataframe):
    if 'date' in dataframe.columns:
        dataframe['date'] = pd.to_datetime(dataframe['date'])
        yr = []
        for date in dataframe['date']:
            xx = getattr(date, dateVar)
            yr.append(str(xx))
        dataframe.loc[:, dateVar] = yr
    return dataframe

def chooseCategory(category, dataframe):
    return dataframe[category]

def cleanDataframe(dataframeWithCategory):
    dataframeWithCategory = dataframeWithCategory.str.lower().str.strip()
    dataframeWithCategory = dataframeWithCategory.replace(r'\W+', ' ', regex=True)
    dataframeWithCategory = dataframeWithCategory.str.encode('ascii', 'ignore').str.decode('ascii')
    #of course there will be more cleaning methods
    return dataframeWithCategory

def showValueCounts(dataframeSlice):
    return dataframeSlice.value_counts()

def deleteBetween(startWord, endWord, dataframe):
    pattern = startWord + "(.*)" + endWord
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern, '', dataframe.iloc[j], flags=re.DOTALL)
    return dataframe

def deleteWord(word, dataframe):
    pattern = word
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,'',dataframe.iloc[j], flags=re.DOTALL)
    return dataframe

def deleteBeginning(start,dataframe):
    pattern =   start + r'[a-zA-Z0-9_.+-]+'
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,"",dataframe.iloc[j])
    return dataframe

def deleteEnd(end,dataframe):
    pattern = r'[a-zA-Z0-9_.+-]+' + end
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,"",dataframe.iloc[j])
    return dataframe


# burasi degisti
'''
df['source'].replace('', np.nan, inplace=True)
df.dropna(subset=['source'], inplace=True)
df['source'] = df['source'].str.replace(' ', '')
df['source'].value_counts()
'''

# df.to_json(r'ai_cntries.json')

frame = getFile("D:/jsons/UK_afterJaccard.json")
print(listColumn(frame))
print(chooseDate("day",frame))
print(listColumn(frame))
print(showValueCounts(cleanDataframe(chooseCategory("source",frame))))
