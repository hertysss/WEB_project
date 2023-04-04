from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class OfficeForm(FlaskForm):
    area = StringField('Площадь', validators=[DataRequired()])
    floor = StringField('Этаж', validators=[DataRequired()])
    bet = StringField('Ставка, в руб за м2/год', validators=[DataRequired()])
    status = SelectField('Статус', choices=['свободен', 'сдан'], validators=[DataRequired()])
    submit = SubmitField('Применить')