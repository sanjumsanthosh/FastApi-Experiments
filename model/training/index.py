import pickle

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.pipeline import Pipeline

from api.schema.train import ModelType
from model import baseModel
from model.training.classifier import tfidf, logistic, trainData, validationData, getSL, vectorizeLabel, outFile, \
    validateionDataPath, customData, combinedData


def train(modelType: ModelType, model: baseModel.Model):
    logRegressionPipeline = Pipeline([
        ('tfidf', tfidf),
        ('logistic', logistic)
    ])
    if modelType == ModelType.custom:
        data = customData
    elif modelType == ModelType.validate:
        data = validationData
    elif modelType == ModelType.combined:
        data = combinedData
    else:
        data = trainData
    Statement, Label = getSL(data)
    logRegressionPipeline.fit(Statement, Label)
    pickle.dump(logRegressionPipeline, open(outFile, 'wb'))
    model.loadModel()


# # validate the model
# Statement_val, Label_val = getSL(validationData)
# predicted = logRegressionPipeline.predict(Statement_val)
# labelArray = vectorizeLabel(Label_val.to_numpy())
#
# # Generate al the metrics
# print('accuracy %s' % accuracy_score(predicted, labelArray))
# print('f1_score %s' % f1_score(predicted, labelArray))
# print('precision_score %s' % precision_score(predicted, labelArray))
# print('recall_score %s' % recall_score(predicted, labelArray))
# print(classification_report(predicted, labelArray))
# print(confusion_matrix(predicted, labelArray))
def validate(modelType: ModelType):
    pickleModel = pickle.load(open(outFile, 'rb'))
    if modelType == ModelType.custom:
        data = customData
    elif modelType == ModelType.validate:
        data = validationData
    elif modelType == ModelType.combined:
        data = combinedData
    else:
        data = trainData
    Statement_val, Label_val = getSL(data)
    predicted = vectorizeLabel(pickleModel.predict(Statement_val))
    labelArray = vectorizeLabel(Label_val.to_numpy())
    return {
        "validationDataLoc": validateionDataPath,
        "accuracy": accuracy_score(predicted, labelArray),
        "f1_score": f1_score(predicted, labelArray),
        "precision_score": precision_score(predicted, labelArray),
        "recall_score": recall_score(predicted, labelArray),
    }
