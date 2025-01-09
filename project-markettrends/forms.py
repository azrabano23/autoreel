# forms.py
from flask_wtf import FlaskForm
from wtforms import SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class CarFilterForm(FlaskForm):
    start_year = SelectField('Start Year', choices=[], coerce=int, validators=[DataRequired()])
    end_year = SelectField('End Year', choices=[], coerce=int, validators=[DataRequired()])
    brands = SelectMultipleField('Brands', choices=[], coerce=str, validators=[DataRequired()])
    fuel_types = SelectMultipleField('Fuel Types', choices=[], coerce=str, validators=[DataRequired()])
    visualization = SelectField('Visualization', choices=[
        ('price_trend', 'Average Price Trend by Year'),
        ('brand_popularity', 'Popularity of Car Brands'),
        ('fuel_efficiency', 'Fuel Efficiency Over Time'),
        ('price_distribution', 'Price Distribution by Fuel Type'),
        ('mileage_price', 'Mileage vs Price Scatter Plot')
    ], validators=[DataRequired()])
    submit = SubmitField('Update Results')
