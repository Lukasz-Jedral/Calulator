import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def get_currencies_full_names_from_csv():
    with open('resources\Dane.csv', newline='') as f:
        reader = csv.reader(f)
        currencies = {}
        for row in reader:
            currencies[row[1]] = {'full_name':row[0],'code':row[1], 'bid':row[2],'ask':row[3]}
    return currencies

currencies = get_currencies_full_names_from_csv()

@app.route('/', methods=['GET','POST'])
def get_main_page():
    if request.method == 'GET':
        return render_template("main.html", currencies=currencies.keys())

    elif request.method == 'POST':
        currency_code = request.form.get('currency')
        currency_amount = request.form.get('HowMuchCurr')
        result = float(currency_amount) * float(currencies[currency_code]['ask'])
        return render_template("result.html",
                               currency_amount = currency_amount,
                               chosen_currency_code = currency_code,
                               calc_result = result)

if __name__=="__main__":
    app.run()


