# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def p5():
    return render_template('projet5.html')

@app.route("/api/", methods = ["POST"])
def tagapi():
    titre = request.form.get('titre')
    contenu = request.form.get('contenu')
    print(titre, contenu)
    return jsonify({'tags': ['exemple']})

if __name__ == "__main__":
    app.run(debug=True)