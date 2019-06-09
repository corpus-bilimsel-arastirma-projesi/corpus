import re
import json
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist


def clean_and_tokenize(file):
    # with open('..\media\\'+filename) as fil:
    data = json.load(file)

    nltk.download('stopwords')
    nltk.download('punkt')

    p = re.compile(r'nonascii|.com|^https?:\/\/.*[\r\n]*|<.*?>|[^a-zA-Z ]+')
    stop_words = stopwords.words("english")

    data["tokens"] = {}

    for docs in data["content"]:
        data["content"][docs] = str(data["content"][docs]).lower()
        data["content"][docs] = p.sub('', str(data["content"][docs]))
        data["content"][docs] = " ".join(data["content"][docs].split())
        data["tokens"][docs] = nltk.word_tokenize(str(data["content"][docs]))
        data["tokens"][docs] = [word.lower() for word in data["tokens"][docs] if word.isalpha() if
                                word not in stop_words]

    data["tok"] = nltk.word_tokenize(str(data["content"]))

    data["tok"] = [word.lower() for word in data["tok"] if word.isalpha() if word not in stop_words]
    dist = FreqDist(data["tok"])
    del data["tok"]
    js = dist.most_common(10)  # 10 is arbitrary I could send whole data and it can be deduced in FE
    # js =json.dumps(js)
    return js


def clean_and_tokenize_v2(file, parameters, most_common):
    # with open('..\media\\'+filename) as fil:
    data = json.load(file)

    nltk.download('stopwords')
    nltk.download('punkt')

    remove_stopwords = False
    remove_punct = False

    for parameter in parameters:
        if parameter == 'Stop Words':
            remove_stopwords = True
        if parameter == 'Punctuations':
            remove_punct = True

    p = re.compile(r'nonascii|.com|^https?:\/\/.*[\r\n]*|<.*?>|[^a-zA-Z ]+')
    stop_words = stopwords.words("english")

    data["tokens"] = {}

    for docs in data["content"]:
        data["content"][docs] = str(data["content"][docs]).lower()
        if remove_punct:
            data["content"][docs] = p.sub('', str(data["content"][docs]))
        data["content"][docs] = " ".join(data["content"][docs].split())
        data["tokens"][docs] = nltk.word_tokenize(str(data["content"][docs]))
        if remove_stopwords:
            data["tokens"][docs] = [word.lower() for word in data["tokens"][docs] if word.isalpha() if
                                    word not in stop_words]

    data["tok"] = nltk.word_tokenize(str(data["content"]))
    if remove_stopwords:
        data["tok"] = [word.lower() for word in data["tok"] if word not in stop_words]
    dist = FreqDist(data["tok"])
    del data["tok"]
    js = dist.most_common(most_common)  # 10 is arbitrary I could send whole data and it can be deduced in FE
    # js = json.dumps(js)
    return js
