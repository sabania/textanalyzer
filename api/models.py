from django.db import models

# Create your models here.


class AnalyzeRequest(models.Model):
    word_count = models.BooleanField(default=False,help_text=("boolean: auswählen, falls dies Anlayseoption erwüscht."))
    most_common_word = models.BooleanField(default=False,help_text=("boolean: auswählen, falls dies Anlayseoption erwüscht."))
    adjective_count = models.BooleanField(default=False,help_text=("boolean: auswählen, falls dies Anlayseoption erwüscht."))
    noun_count = models.BooleanField(default=False,help_text=("boolean: auswählen, falls dies Anlayseoption erwüscht."))
    verb_count = models.BooleanField(default=False,help_text=("boolean: auswählen, falls dies Anlayseoption erwüscht."))
    file = models.FileField(default=None,help_text=("file: Datei, die analysiert werden soll."))
