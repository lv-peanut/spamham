from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle
import json
from tokenizer import tokenizer


app = Flask(__name__)

def spamham(text):

    """Spamham classifier function

    Inputs
    ------

    text : list [str,]
        list of strings to classify

    Returns
    -------

    list [str, ]
        list of classifications either ham or spam
    
    """

    X = vectorizer.transform(text)
    prediction = classifier.predict(X)

    return ['spam' if p == 1 else 'ham' for p in prediction]


@app.route('/api/spamham', methods=['POST'])
def makecalc():
    data = request.get_json()
    print(data)
    res = spamham(data)

    return jsonify(res)

if __name__ == '__main__':

    vecotrizer_path = 'models/vectorizer.pkl'
    with open(vecotrizer_path, 'rb') as f:
        vectorizer = pickle.load(f)

    classifier_path = 'models/classifier.pkl'
    with open(classifier_path, 'rb') as f:
        classifier = pickle.load(f)

    app.run(debug=True, host='0.0.0.0')