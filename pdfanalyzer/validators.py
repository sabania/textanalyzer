# -*- coding: utf-8 -*-

from django import forms

from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def clean_content(self):
    print('executed')
    content = self.cleaned_data['content']
    content_type = content.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES:
        if content._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    else:
        raise forms.ValidationError(_('Dateityp wird nicht unterstützt!'))
    return content


"""
def clean_content(form):
    content = form.cleaned_data['content']
    
    
    # HttpRequest.content_type: A string representing the MIME type of the request, parsed from the CONTENT_TYPE header.

    content_type = content.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES:
        if content._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    else:
        raise forms.ValidationError(_('Dateityp wird nicht unterstützt!'))
    return content
"""

# https://docs.djangoproject.com/en/2.0/ref/files/uploads/

def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise forms.ValidationError('Die Datei ist zu gross!')

# Like any data supplied by the user, you shouldn’t trust that the uploaded 
#file is actually this type. You’ll still need to validate that the file 
#contains the content that the content-type header claims – “trust but verify.”
def file_type(value):
    if value.content_type != 'application/pdf':
        raise forms.ValidationError('Kein pdf!')