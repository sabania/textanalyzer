# -*- coding: utf-8 -*-
from django.contrib.sessions.backends.db import SessionStore

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import UploadFile

from .models import Textfile

from django.urls import reverse

"""
from .nltkanalysis import test
from .nltkanalysis import pdfToText
from .nltkanalysis import texttokenize
from .nltkanalysis import mostfreqword
"""
from .nltkanalysis import Nltkanalysis
from .pdfhandler import Pdfhandler

# dropzone js upload
# https://amatellanes.wordpress.com/2013/11/05/dropzonejs-django-how-to-build-a-file-upload-form/
def upload_file(request):
    if not request.session.session_key:
        request.session.save()
    
    print('upload_file')
    form = UploadFileForm(request.POST, request.FILES)
    context = {'form': form}
    
    if request.method == 'POST':
        if form.is_valid():
            print('dropzone post')
            newfile = UploadFile(file = request.FILES['file'])
            newfile.session_key = request.session.session_key
            newfile.save()
            return HttpResponseRedirect(reverse('pdfanalyzer:upload')) 
        else:
            form = UploadFileForm()
         
    return render(request, 'pdfanalyzer/upload.html', context)




def analyse(request):

    for file in UploadFile.objects.filter(analysed = False, session_key = request.session.session_key):
        pdfread = Pdfhandler(file.filename())
        
        # Analyse 
        measurements = request.POST.get('measurements')
        analysis = Nltkanalysis(pdfread.pdfToText())
        
                
        # http://www.nltk.org/_modules/nltk/text.html
        # http://www.nltk.org/api/nltk.html#nltk.text.TextCollection
        #textcollection.append(analysis.tokenizedtext)

        analysis.runAnalysis(measurements)
        
        pdfread.deleteFile()
        file.analysed = True
        file.word_count = analysis.wordCount
        file.most_common_word = analysis.mostCommonWord
        file.adjective_count = analysis.adjectivecount
        file.noun_count = analysis.nouncount
        file.verb_count = analysis.verbcount
        file.save()
        
    # create PDF Report
    Pdfhandler.createPdfReport()

    analysedfiles = UploadFile.objects.filter(session_key = request.session.session_key)
    context = {'analysedfiles': analysedfiles}
        
    return render(request, 'pdfanalyzer/analyse.html', context)

    