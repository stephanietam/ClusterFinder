"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, flash, request
from Form import LoginForm
import pickle
from ClusterFinder import app

app.config.update(dict(
    SECRET_KEY="1234567890",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# Unpickle the model
filename = "MarketingProfileModel.sav"
infile = open(filename, 'rb')
loadedModel = pickle.load(infile)
infile.close()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    form = LoginForm(request.form)
    return render_template(
        'index.html',
        title='Cluster Finder',
        form=form
    )

@app.route('/predict', methods=['GET'])
def run_model():
    # Get dropbox values
    competency = int(request.args.get('competency'))
    product = int(request.args.get('product'))
    country = int(request.args.get('country'))

    # Set competency list
    if competency==0:
        competency_list = [1,0]
    else:
        competency_list = [0,1]

    # Set product list
    product_weights = [100,50,40,10,30,20,20,10,90,70,100,50,10,70,50,40,50,50,30,30,20,90]
    product_list = []
    for i in range(len(product_weights)):
        if i==product:
            product_list.append(product_weights[i])
        else:
            product_list.append(0)

    # Set country list
    country_list = [0 for i in range(215)]
    country_list[country] = 1

    # Combine all lists
    parameters = competency_list + product_list + country_list

    # Get the predicted cluster from the model
    prediction = loadedModel.predict([parameters])[0]

    return render_template(
        'index.html',
        title="Cluster Finder",
        prediction=prediction,
        submitted=True,
        form = LoginForm(request.form)
    )