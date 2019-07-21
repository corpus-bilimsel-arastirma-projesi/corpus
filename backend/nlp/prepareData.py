# -*- coding: utf-8 -*-
import pandas as pd
import re


def column_names(data_frame):
    return data_frame.columns


def column_mapping(columns, data_frame):
    data_frame.rename(columns={columns['content']: 'content',
                               columns['date']: 'date',
                               columns['source']: 'source',
                               columns['title']: 'title',
                               columns['docid']: 'docid'
                               },
                      inplace=True)
    return data_frame.to_json()


# to get file and convert into dataframe
def json_to_data_frame(file):
    data_frame = pd.read_json(file)  # currently only json files
    return data_frame


def data_frame_to_json(file):
    data_frame = pd.read_json(file)  # currently only json files
    return data_frame.to_json()


# to concat many files and use them together
def file_concat(file_list):
    data_frame = pd.concat(file_list, ignore_index=True)
    return data_frame.to_json()


# user may select the date(day,month,year) and create new column to use it later
def choose_date(date_var, data_frame):
    if 'date' in data_frame.columns:
        data_frame['date'] = pd.to_datetime(data_frame['date'])
        yr = []
        for date in data_frame['date']:
            xx = getattr(date, date_var)
            yr.append(str(xx))
        data_frame.loc[:, date_var] = yr
    return data_frame.to_json()


# optional cleaning methods
# to delete all characters between given words (included given words)
def delete_between(start_word, end_word, data_frame, column):
    pattern = start_word + "(.*)" + end_word
    for j in range(len(data_frame)):
        data_frame[column].iloc[j] = re.sub(pattern, '', data_frame[column].iloc[j], flags=re.DOTALL)
    return data_frame.to_json()


# to delete specific word
def delete_word(word, data_frame, column):
    pattern = r" " + word + " "
    for j in range(len(data_frame)):
        data_frame[column].iloc[j] = re.sub(pattern, ' ', data_frame[column].iloc[j], flags=re.DOTALL)
    return data_frame.to_json()


# delete words that contains given characterset
def delete_contain(word, data_frame, column):
    pattern = word
    for j in range(len(data_frame)):
        data_frame[column].iloc[j] = re.sub(pattern, '', data_frame[column].iloc[j], flags=re.DOTALL)
    return data_frame.to_json()


# to delete words that starts with given characterset
def delete_beginning(start, data_frame, column):
    pattern = start + r'[a-zA-Z0-9_.+-]+'
    for j in range(len(data_frame)):
        data_frame[column].iloc[j] = re.sub(pattern, "", data_frame[column].iloc[j])
    return data_frame.to_json()


# to delete words that ends with given characterset
def delete_end(end, data_frame, column):
    pattern = r'[a-zA-Z0-9_.+-]+' + end
    for j in range(len(data_frame)):
        data_frame[column].iloc[j] = re.sub(pattern, "", data_frame[column].iloc[j])
    return data_frame.to_json()


# replaces list of words with given targetword
def replace_words(word_list, target_word, data_frame):
    dict = {}
    for word in word_list:
        dict.update({word: target_word})
    data_frame = pd.DataFrame(data_frame)
    data_frame = data_frame.replace(dict, regex=True)
    return data_frame.to_json()


# burasi degisti
'''
df['source'].replace('', np.nan, inplace=True)
df.dropna(subset=['source'], inplace=True)
df['source'] = df['source'].str.replace(' ', '')
df['source'].value_counts()
'''


# df.to_json(r'ai_cntries.json')

# replaces date format from 03/07/1970 to 03-07-1970

# dataframe olarak al dataframeDate oalrak değil.
def replace_date_format(data_frame):
    for j in range(len(data_frame['date'])):
        data_frame['date'].iloc[j] = re.sub(r'/', '-', data_frame['date'].iloc[j], flags=re.DOTALL)
    return data_frame


# gives columns(source, content etc.) of dataframe as a list
def list_column(data_frame):
    return list(data_frame.columns)


# gives slice of dataframe with selected category
def choose_category(category, data_frame):
    return data_frame[category]


# cleaning given dataframeslice(dataframeslice means = dataframe["category"])

# dataframe değiştirmek istediği kategori haricinde diğerleri olduğu gibi kalacak, kategori için bu temizliği yapıp updated dataframei return et.
def clean_data_frame(data_frame, category):
    data_frame[category] = data_frame[category].str.lower().str.strip()
    data_frame[category] = data_frame[category].replace(r'\W+', ' ', regex=True)
    data_frame[category] = data_frame[category].str.encode('ascii', 'ignore').str.decode('ascii')
    # of course there will be more cleaning methods
    return data_frame


# value count of given dataframeslice
def show_value_counts(data_frame_slice):
    return data_frame_slice.value_counts()


