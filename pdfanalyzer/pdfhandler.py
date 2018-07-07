# -*- coding: utf-8 -*-

# Doc: https://pythonhosted.org/PyPDF2/PdfFileWriter.html
# https://stackoverflow.com/questions/2252726/how-to-create-pdf-files-in-python
# https://pypi.org/project/pdfkit/ html -> pdf
# reportLab

import PyPDF2
#import pdfkit
from reportlab.pdfgen import canvas


import os

class Pdfhandler(object):
    def __init__(self,
                 filename):
        self.filename = filename
        self.absoluteFilePath = self.__absoluteFilePath()

    def __absoluteFilePath(self):
        script_dir = os.path.dirname(__file__) # absolute dir the script is in
        # ".." moves one folder back
        # absoluteFilePath = os.path.join(script_dir, "..", "textfiles", "textfiles", self.filename)
        absoluteFilePath = os.path.join(script_dir, "..", "tmpfiles", "textfiles", self.filename)
        return absoluteFilePath
    
    def deleteFile(self):
        os.remove(self.absoluteFilePath)

    def pdfToText(self):
        text = ''
        pdf = open(self.absoluteFilePath, 'rb')
        fileReader = PyPDF2.PdfFileReader(pdf)
        for page in fileReader.pages:
            text = text + page.extractText().replace('\n', '')
        pdf.close()
        return text
    
    @staticmethod
    def createPdfReport():
        script_dir = os.path.dirname(__file__)
        absoluteFilePath = os.path.join(script_dir, "..", "tmpfiles", "reports", "Report.pdf")
        c = canvas.Canvas(absoluteFilePath)
        # c = canvas.Canvas("/tmpfiles/reports/Report.pdf")
        c.drawString(100,100,"PDFanalyzer Report")
        c.showPage()
        c.save()
    
    """
    
    def htmlReportToPdf(self):
        pdfkit.from_url('http://google.com', 'out.pdf')
        
        
        from django.test import Client
        c = Client()
        response = c.get('/mymodel/1')
        content = response.content
    """



