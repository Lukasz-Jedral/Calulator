from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

class RadioForm(FlaskForm):
    radio_field = RadioField(label = "Co zamierzasz zrobić?:",choices=[('browse','Przeglądaj bibliotekę'),
                                        ('add','Dodaj pozycję do biblioteki'),
                                        ('delete','Usuń pozycję z biblioteki')])
    submit_field = SubmitField("Wykonaj")

class AddNewBookForm(FlaskForm):
    title = StringField('Tytuł:', validators=[DataRequired()])
    author = StringField('Autor:', validators=[DataRequired()])
    description = StringField('Opis:', validators=[DataRequired()])
    published = IntegerField('Rok wydania:', validators=[DataRequired()])
    publisher = StringField('Wydawca:', validators=[DataRequired()])
    cover = FileField('Okładka:',_name='file',validators=[FileRequired()])
    submit_field = SubmitField("Dodaj do biblioteki")
    cover2 = FileField()
