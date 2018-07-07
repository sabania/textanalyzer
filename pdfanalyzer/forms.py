# -*- coding: utf-8 -*-

from django import forms

"""
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
"""


from .models import UploadFile
    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__' # Or a list of the fields that you want to include in your form

