# -*- coding: utf-8 -*-
import pandas as pd
import re

#to get file and convert into dataframe
def getFile(file):
    dataFrame = pd.read_json(file) #currently only json files
    return dataFrame

#to concat many files and use them together
def fileConcat(fileList):
    dataFrame = pd.concat(fileList,ignore_index=True)
    return dataFrame

#gives columns(source, content etc.) of dataframe as a list
def listColumn(dataframe):
    return list(dataframe.columns)

#user may select the date(day,month,year) and create new column to use it later
def chooseDate(dateVar,dataframe):
    if 'date' in dataframe.columns:
        dataframe['date'] = pd.to_datetime(dataframe['date'])
        yr = []
        for date in dataframe['date']:
            xx = getattr(date, dateVar)
            yr.append(str(xx))
        dataframe.loc[:, dateVar] = yr
    return dataframe

#replaces date format from 03/07/1970 to 03-07-1970
def replaceDateFormat(dataframeDate):
    for j in range(len(dataframeDate)):
        dataframeDate.iloc[j] = re.sub(r'/', '-', dataframeDate.iloc[j], flags=re.DOTALL)
    return dataframeDate

#gives slice of dataframe with selected category
def chooseCategory(category, dataframe):
    return dataframe[category]

#cleaning given dataframeslice(dataframeslice means = dataframe["category"])
def cleanDataframe(dataframeWithCategory):
    dataframeWithCategory = dataframeWithCategory.str.lower().str.strip()
    dataframeWithCategory = dataframeWithCategory.replace(r'\W+', ' ', regex=True)
    dataframeWithCategory = dataframeWithCategory.str.encode('ascii', 'ignore').str.decode('ascii')
    #of course there will be more cleaning methods
    return dataframeWithCategory

#value count of given dataframeslice
def showValueCounts(dataframeSlice):
    return dataframeSlice.value_counts()

#optional cleaning methods
#to delete all characters between given words (included given words)
def deleteBetween(startWord, endWord, dataframe):
    pattern = startWord + "(.*)" + endWord
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern, '', dataframe.iloc[j], flags=re.DOTALL)
    return dataframe

#to delete specific word
def deleteWord(word, dataframe):
    pattern = r" "+ word+ " "
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,' ',dataframe.iloc[j], flags=re.DOTALL)
    return dataframe

#delete words that contains given characterset
def deleteContain(word,dataframe):
    pattern = word
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,'',dataframe.iloc[j], flags=re.DOTALL)
    return dataframe

#to delete words that starts with given characterset
def deleteBeginning(start,dataframe):
    pattern =   start + r'[a-zA-Z0-9_.+-]+'
    for j in range(len(dataframe)):
        dataframe.iloc[j] = re.sub(pattern,"",dataframe.iloc[j])
    return dataframe

#to delete words that ends with given characterset
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
