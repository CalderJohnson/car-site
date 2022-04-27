"""Routes to the websites landing page"""
from flask import Blueprint, render_template, request
from website.data import getCarData

index = Blueprint('homepage', __name__)

@index.route('/app', methods=['GET', 'POST'])
def main():
    """Index page for the website"""
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        #here are the variables from their input form in the index.html
        make = request.form['maker']
        model = request.form['model']
        year = request.form['year']

        data = getCarData(make, model, year)

        return render_template('search.html', results=data["records"][:10])
