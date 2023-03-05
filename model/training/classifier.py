import os
import sys

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd
from model.training.Config import Config

configPath = os.path.join(os.path.dirname(__file__), '../../config.yaml')
config = Config(configPath)

# Getting the configs
tfidf_config = config.get('model.tfidf')
# tfidf_config : {'stopWords': 'english', 'ngramRange': [1, 2], 'useIdf': True, 'smoothIdf': True}
logistic_config = config.get('model.logisticRegression')
# logistic_config : {'C': 1.0, 'penalty': 'l2'}

tfidf = TfidfVectorizer(
    stop_words=tfidf_config['stopWords'],
    ngram_range=tuple(tfidf_config['ngramRange']),
    use_idf=tfidf_config['useIdf'],
    smooth_idf=tfidf_config['smoothIdf']
)

logistic = LogisticRegression(
    C=logistic_config['C'],
    penalty=logistic_config['penalty']
)


def vectorizeLabelDf(data):
    data['Label'] = vectorizeLabel(data['Label'].to_numpy())
    return data


def vectorizeLabel(labelArray):
    if labelArray.dtype == 'bool':
        return labelArray
    return np.vectorize(lambda x: True if x == 'TRUE' else False)(labelArray)


# datafram
testDataPath = config.get("model.files.trainFile")
validateionDataPath = config.get("model.files.validationFile")
customDataPath = config.get("model.files.customFile")

trainData = pd.read_csv(testDataPath).dropna()
validationData = pd.read_csv(validateionDataPath).dropna()
customData = pd.read_csv(customDataPath).dropna()

trainData = vectorizeLabelDf(trainData)
validationData = vectorizeLabelDf(validationData)
customData = vectorizeLabelDf(customData)

combinedData = pd.concat([trainData, validationData, customData], ignore_index=True)

outFile = config.get("model.modelOutFile")


# data is in format Statement, Label
# function which takes data and returns Statement and Label
def getSL(data):
    return data['Statement'], data['Label']
