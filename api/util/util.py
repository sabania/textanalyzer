from pdfanalyzer.nltkanalysis import Nltkanalysis
from pdfanalyzer.pdfhandler import Pdfhandler
from pdfanalyzer.models import UploadFile

def calcmeasurement(data):
    measurement = 0
    if data['word_count'] == 'true':
        measurement = measurement +1
    else:
        measurement = measurement -1
    if data['most_common_word'] == 'true':
        measurement = measurement +10
    else:
        measurement = measurement -10
    if data['adjective_count'] == 'true':
        measurement = measurement +100
    else:
        measurement = measurement -100
    if data['noun_count'] == 'true':
        measurement = measurement +1000
    else:
        measurement = measurement -1000
    if data['verb_count'] == 'true':
        measurement = measurement +10000
    else:
        measurement = measurement -10000
    return  measurement


def analyse(sessionkey, measurements):
    # print('Analysen: ', request.POST.get('measurements'))
    # textcollection = []

    for file in UploadFile.objects.filter(analysed=False, session_key=sessionkey):
        pdfread = Pdfhandler(file.filename())

        # Analyse
        analysis = Nltkanalysis(pdfread.pdfToText())

        # http://www.nltk.org/_modules/nltk/text.html
        # http://www.nltk.org/api/nltk.html#nltk.text.TextCollection
        # textcollection.append(analysis.tokenizedtext)

        analysis.runAnalysis(measurements)

        pdfread.deleteFile()
        file.analysed = True
        file.word_count = analysis.wordCount
        file.most_common_word = analysis.mostCommonWord
        file.adjective_count = analysis.adjectivecount
        file.noun_count = analysis.nouncount
        file.verb_count = analysis.verbcount
        file.save()

    analysedfiles = UploadFile.objects.filter(session_key =sessionkey)

    return analysedfiles