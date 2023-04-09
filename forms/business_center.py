from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class Business_centerForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    building = StringField('Строение', validators=[DataRequired()])
    district = StringField('Округ', validators=[DataRequired()])
    metro = StringField('Станция метро', validators=[DataRequired()])
    total_area = StringField('Общая площадь, в м2', validators=[DataRequired()])
    klass = SelectField('Класс', choices=['A', 'B', 'C'], validators=[DataRequired()])
    floors = StringField('Количество этажей', validators=[DataRequired()])
    lift = SelectField('Наличие лифта', choices=['да', 'нет'], validators=[DataRequired()])
    parking = SelectField('Наличие парковки', choices=['да', 'нет'], validators=[DataRequired()])
    contact = StringField('Контактная информация арендодателя', validators=[DataRequired()])
    submit = SubmitField('Применить')
