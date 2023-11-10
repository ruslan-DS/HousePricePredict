import joblib
def predict(data):
    cbr = joblib.load("cbr_model.sav")
    return cbr.predict(data)