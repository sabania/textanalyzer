# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.sessions.backends.db import SessionStore as DBStore

from django.contrib.sessions.base_session import AbstractBaseSession

import os

#from .validators import clean_content

class Textfile(models.Model):
    textfile_name = models.CharField(max_length=20)
    textfile_size = models.IntegerField()
    
    def __str__(self):
        return self.textfile_name
    
# Model field shows which Model your Form would be created from and 
# Fields field shows which fields from the Model class to show in your new Form.

# https://docs.djangoproject.com/en/2.0/topics/http/sessions/

class UploadFile(models.Model):
    file = models.FileField(upload_to='textfiles/')
    session_key = models.CharField(max_length=40, default = '0000', blank = True)
    analysed = models.BooleanField(default = False)
    word_count = models.IntegerField(default = 0, blank = True, null = True)
    most_common_word = models.CharField(max_length=100, default = '0000', blank = True)
    adjective_count = models.IntegerField(default = 0, blank = True, null = True)
    noun_count = models.IntegerField(default = 0, blank = True, null = True)
    verb_count = models.IntegerField(default = 0, blank = True, null = True)

    #@property
    def filename(self):
        return os.path.basename(self.file.name)
    
    # If the method doesn't require any arguments, you can use the @property decorator and access it normally in the template.
    @property
    def deleteEntry(self):
        print('delete')
        self.delete()

