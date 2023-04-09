from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SelectField, SubmitField, FileField, IntegerField
from wtforms.validators import DataRequired


class Business_centerForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    building = StringField('Строение', validators=[DataRequired()])
    district = StringField('Округ', validators=[DataRequired()])
    metro = StringField('Станция метро', validators=[DataRequired()])
    total_area = IntegerField('Общая площадь, в м2', validators=[DataRequired()])
    klass = SelectField('Класс', choices=['A', 'B', 'C'], validators=[DataRequired()])
    floors = IntegerField('Количество этажей', validators=[DataRequired()])
    lift = SelectField('Наличие лифта', choices=['да', 'нет'], validators=[DataRequired()])
    parking = SelectField('Наличие парковки', choices=['да', 'нет'], validators=[DataRequired()])
    contact = StringField('Контактная информация арендодателя', validators=[DataRequired()])
    photo = FileField('Фотография бизнес-центра', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Применить')
