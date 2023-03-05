from api.schema import predict
import model.baseModel


def predict(request: str, model: model.baseModel.Model):
    predict_prob = model.predict(request)
    # predict_prob contains a list of probabilities for each class (good, bad)
    isGood = predict_prob[0][0] > 0.5
    confidence = predict_prob[0][0] if isGood else predict_prob[0][1]
    return {
        "score": confidence,
        "isGood": isGood
    }
