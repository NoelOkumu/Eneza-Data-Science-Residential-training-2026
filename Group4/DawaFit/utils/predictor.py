#!/usr/bin/env python3

import joblib

class ResistancePredictor:

    def __init__(self):

        self.models = {
            "3TC": joblib.load("models/best_model_3TC.pkl"),
            "ABC": joblib.load("models/best_model_ABC.pkl"),
            "AZT": joblib.load("models/best_model_AZT.pkl"),
            "TDF": joblib.load("models/best_model_TDF.pkl")
        }

    def predict(self, X):

        predictions = {}

        for drug, model in self.models.items():
            predictions[drug] = model.predict(X)[0]

        return predictions
