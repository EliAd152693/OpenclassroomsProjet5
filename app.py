from flask import Flask, request, jsonify, render_template
from wtforms import Form, TextAreaField, validators
import joblib
import pandas as pd
import numpy as np
import pickle
import gensim
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing

def predict_tag(document):
    nlp_model = open('pkl_objects/model.pkl', 'rb')
    model = joblib.load(nlp_model)
    tfidf_model = open('pkl_objects/tfidf.pkl', 'rb')
    tfidf = joblib.load(tfidf_model)
    encoder_model = open('pkl_objects/encoder.pkl', 'rb')
    encoder = joblib.load(encoder_model)

    tokenized_input = gensim.utils.simple_preprocess(document, deacc=True)
    tfidf_input = tfidf.transform(tokenized_input)
    num_pred = model.predict(tfidf_input)
    prediction = np.array(encoder.inverse_transform(num_pred))
    return np.array2string(prediction)


app = Flask(__name__)

class QuestionForm(Form):
    sentence = TextAreaField('', 
                                [validators.DataRequired(), validators.length(min=15)])

    
@app.route("/", methods=['GET','POST'])
def index():
    form = QuestionForm(request.form)
    return render_template('questionform.html', form=form)


@app.route("/results", methods=['GET','POST'])
def results():
    form = QuestionForm(request.form)
    if request.method == 'POST' and form.validate():
        data = request.form.get('sentence')
        pred = predict_tag(data)
        return render_template('results.html',
                              content = data,
                              prediction = pred)

    return render_template('questionform.html', form=form)

@app.route("/api/", methods=['POST'])
def predict():
    data = request.get_json()
    prediction = np.array(predict_tag(data))
    return jsonify(np.array2string(prediction))

if __name__ == "__main__":
    app.run(debug=True)