# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,NumberRange

class addproduct(FlaskForm):
    prodname = StringField('Product Name', validators=[DataRequired()])
    prodqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    prodsubmit = SubmitField('Save Changes')

class editproduct(FlaskForm):
    editname = StringField('Product Name', validators=[DataRequired()])
    editqty = IntegerField('Quantity', validators=[NumberRange(min=5, max=1000000),DataRequired()])
    editsubmit = SubmitField('Save Changes')

class addlocation(FlaskForm):
    locname = StringField('Location Name', validators=[DataRequired()])
    locsubmit = SubmitField('Save Changes')

class editlocation(FlaskForm):
    editlocname = StringField('Location Name', validators=[DataRequired()])
    editlocsubmit = SubmitField('Save Changes')

class moveproduct(FlaskForm):
    mprodname = SelectField('Product Name', choices=[], validators=[DataRequired()])
    src = SelectField('Source Location', choices=[], validators=[DataRequired()])
    destination = SelectField('Destination Location', choices=[], validators=[DataRequired()])
    mprodqty = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    movesubmit = SubmitField('Move Product')

