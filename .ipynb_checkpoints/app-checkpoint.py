# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
import joblib
import json
import pandas as pd
import numpy as np
import pickle
import gensim
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing

app = Flask(__name__)

@app.route("/api/", methods = ["POST"])
def predict():
    data = request.get_json()
    tokenized_input = gensim.utils.simple_preprocess(data, deacc=True)
    tfidf_input = tfidf.transform(tokenized_input)
    num_pred = model.predict(tfidf_input)
    prediction = np.array(encoder.inverse_transform(num_pred))
    return jsonify(np.array2string(prediction))

if __name__ == "__main__":
    nlp_model = open('model.pkl', 'rb')
    model = joblib.load(nlp_model)
    tfidf_model = open('tfidf.pkl', 'rb')
    tfidf = joblib.load(tfidf_model)
    encoder_model = open('encoder.pkl', 'rb')
    encoder = joblib.load(encoder_model)
    app.run(debug=True)