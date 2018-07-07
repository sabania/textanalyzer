# PDFanalyzer

PDFanalyzer ist ein Django Webservice der es ermöglicht den Textinhalt von PDF-Dateien 
statistischen Analysen zu unterziehen. Die auszuführenden Analysen können beliebig gewählt werden.
Nach der Durchführung der Analysen werden die Resultate in einer Tabelle angezeigt.

Features:
- eine oder mehrere PDF-Dateien per Drag and Drop hochladbar
- maximale Dateigrösse 2MB
- andere Dateitypen werden nicht akzeptiert
- API Zugang

Python: Version 3.0.6

Installation der notwendigen Pakete:
- $: pip install django
- $: pip install nltk
- $: pip install reportlab
- $: pip install pypdf2
- $: pip install pyyaml
- $: pip install djangorestframework
- $: pip install django-rest-swagger

Installation:
- $: virtualenv env-name
- $: cp textanalyzer /env-name
- $: activate env-name
- (env-name)$: cd env-name/Scripts

Server starten:
- (env-name)$: cd textanalyzer
- (env-name)$: python manage.py runserver 0.0.0.0:8080
