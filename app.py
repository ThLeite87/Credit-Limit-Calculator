from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            sales = int(request.form['sales'])
            payment_terms = int(request.form['payment_terms'])
            season = int(request.form['season'])
            credit_recommended = "{:,.0f}".format(
                sales / 360 * payment_terms * (1 + season / 100)
            )
            result = {
                'sales': sales,
                'payment_terms': payment_terms,
                'season': season,
                'credit_recommended': credit_recommended
            }
        except ValueError:
            result = 'error'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
