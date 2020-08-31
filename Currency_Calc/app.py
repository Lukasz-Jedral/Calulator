#import csv
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/currency_calc/main', methods=['GET'])
def get_main_page():
    if request.method == 'GET':
        return render_template("main.html")


if __name__=="__main__":
    app.run()

#with open('resources\Dane.csv',newline='') as f:
   # reader = csv.reader(f)
   # for row in reader:
    #    print(row)