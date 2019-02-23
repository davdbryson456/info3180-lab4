
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
import os

class UploadForm(Form):
    photo = FileField('photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    
    
