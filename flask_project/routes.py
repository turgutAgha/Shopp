from flask import render_template, request

from flask_project import app
from flask_project.business_layer import displayer


@app.route("/")
@app.route("/home", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        search_term = request.form['search']
        websites = request.form.getlist('website')
        sort_type = request.form['isort']
        currency = request.form['icurrency']
        min_pr = request.form['min_pr']
        max_pr = request.form['max_pr']

        try:
            min_pr = float(min_pr)
        except:
            min_pr = 0
        try:
            max_pr = float(max_pr)
        except:
            max_pr = 1000000

        price_range = [float(min_pr), float(max_pr)]
        diss = displayer.Displayer(search_term, websites, sort_type, currency, price_range)
        posts = diss.display()

        return render_template('home.html', posts=posts)

    return render_template('home.html')
