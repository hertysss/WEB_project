from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class OfficeForm(FlaskForm):
    area = IntegerField('Площадь', validators=[DataRequired()])
    floor = IntegerField('Этаж', validators=[DataRequired()])
    bet = IntegerField('Ставка, в руб за м2/год', validators=[DataRequired()])
    status = SelectField('Статус', choices=['свободен', 'сдан'], validators=[DataRequired()])
    submit = SubmitField('Применить')