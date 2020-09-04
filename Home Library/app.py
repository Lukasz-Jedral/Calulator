import os
from flask import Flask, request, render_template, redirect, url_for
from forms import RadioForm, AddNewBookForm
from models import homelibrary

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config.from_object(__name__)#completnie nie wiem co robi ta linia
app.config["SECRET_KEY"] = "bardzosekretnehaslo"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/home_library/main", methods=["GET", "POST"])
def load_main_view():
    form = RadioForm()
    if request.method == "POST":
        response = form.radio_field.data
        if response == 'browse':
            return redirect(url_for('display_full_list'))

        if response == 'add':
            return redirect(url_for('add_new_book'))

    return render_template('main.html', form = form)

@app.route("/home_library/add_new_book", methods=["GET", "POST"])
def add_new_book():
    form = AddNewBookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            temp_dict = request.form.to_dict()
            temp_dict.pop('submit_field')
            file = request.files['cover']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            temp_dict['file_name'] = file.filename
            homelibrary.create(temp_dict)
            homelibrary.save_all()
        return render_template('upload_succesful.html')

    return render_template('add_new_book.html', form = form)

@app.route("/home_library/full_list", methods=["GET", "POST"])
def display_full_list():
    books = homelibrary.all()
    return render_template('full_list.html', books = books)

@app.route("/home_library/book/<int:book_id>", methods=["GET", "POST"])
def book_details(book_id):
    book = homelibrary.get(book_id - 1)
    return render_template('book_details.html',
                           book = book,
                           book_id = book_id)

@app.route("/home_library/book_update/<int:book_id>", methods=["GET", "POST"])
def book_update(book_id):
    book = homelibrary.get(book_id-1)
    form = AddNewBookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            temp_dict = request.form.to_dict()
            temp_dict.pop('submit_field')
            file = request.files['cover']
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            temp_dict['file_name'] = file.filename
            homelibrary.update(book_id-1,temp_dict)
            homelibrary.save_all()
            return render_template('upload_succesful.html')
    return render_template('book_update.html',
                           book = book,
                           form = form)


if __name__ == '__main__':
    app.run(debug=True)