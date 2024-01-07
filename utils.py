import pickle

cv = pickle.load(open("models/cv.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))


def model_predict(txt_msg):
    if txt_msg == "":
        return ""
    tokenized_msg = cv.transform([txt_msg])  # X
    prediction = clf.predict(tokenized_msg)

    prediction = 1 if prediction == 1 else -1
    return prediction
