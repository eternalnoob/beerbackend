from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import DecimalField
from wtforms.validators import NumberRange, ValidationError

class BeerForm(Form):
    beer_name = StringField('Beer Name', validators=[DataRequired()])
    abv = DecimalField('Alcohol %', validators=[DataRequired()])
    hoppiness = DecimalField('Hoppiness', validators=[DataRequired(), NumberRange(0, 10)])
    bitterness = DecimalField('Bitterness', validators=[DataRequired(), NumberRange(0, 10)])
    fruitiness = DecimalField('Fruitiness', validators=[DataRequired(), NumberRange(0, 10)])

    def check_abv(form, field):
        if field.data <= 0:
            raise ValidationError('Field Must be Positive')
        if field.data >= 100:
            raise ValidationError('Field must be Less than 100')
