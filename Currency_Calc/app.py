import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def get_currencies_full_names_from_csv(integer):
    with open('resources\Dane.csv', newline='') as f:
        reader = csv.reader(f)
        currencies = []
        for row in reader:
            currencies.append(row[0])
    return currencies

def get_whole_row_for_chosen_currency_form_csv_file(currency_ful_name):
    with open('resources\Dane.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            for item in row:
                if item == currency_full_name:
                    f_result = row
    return f_result


@app.route('/currency_calc/main', methods=['GET','POST'])
def get_main_page():
    if request.method == 'GET':
        currencies = get_currencies_full_names_from_csv(0)
        return render_template("main.html", currencies=currencies)

    elif request.method == 'POST':
        currency_full_name = request.form['currency']
        currency_amount = request.form.get('HowMuchCurr')
        currency_row = get_whole_row_for_chosen_currency_form_csv_file(currency_full_name)
        result = float(currency_amount) * float(currency_row[3])
        currency_code = currency_row[1]
        return render_template("result.html", choosen_currency_code = currency_code, calc_result = result)

if __name__=="__main__":
    app.run()


