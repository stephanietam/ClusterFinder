from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    competency_list = enumerate(["Gold Competencies","Silver Competencies"])
    product_list = enumerate(["Azure","Dynamics365Enterprise","DeveloperTools","EnterpriseMobilityAndSecurity","Dynamics365Business" ,"Exchange","DynamicsAX" ,"GP", "Microsoft365","PowerBI" ,"Office","Project" ,"SL","SQL","SharePoint","SkypeForBusiness","SurfaceHub","Surface","Teams","Yammer","Visio","Windows"])
    country_list = enumerate(["US","GB","GE","FR","AU"])
    
    competency = SelectField('Competency', choices=competency_list, default=1)
    product = SelectField('Product', choices=product_list, default=1)
    country = SelectField('Country', choices=country_list, default=1)
    submit = SelectField('Submit')