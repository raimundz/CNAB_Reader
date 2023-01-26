from django.db import models
from django import forms

class UploadFile(forms.Form):
  file = forms.FileField()