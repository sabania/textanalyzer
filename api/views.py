from rest_framework.response import Response
from api.serializer import AnalyzeRequestSerializer, AnalyzeResponceSerializer
from api.models import AnalyzeRequest
from rest_framework import generics
from pdfanalyzer.models import UploadFile
import uuid
from api.util import util

# Create your views here.



class AnalyzeRequestAPIView(generics.CreateAPIView):
    """

    post:
    Analyseoptionen auswählen und Datei raufladen, die analysiert werden soll.

     """

    serializer_class = AnalyzeRequestSerializer
    queryset = AnalyzeRequest.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        measurment = util.calcmeasurement(data=data)
        uploadfile = UploadFile()
        file = request.FILES['file']
        uploadfile.session_key = uuid.uuid4()
        uploadfile.file = file
        uploadfile.save()
        analyzedFiles = util.analyse(sessionkey=uploadfile.session_key,measurements=measurment)
        serializer = AnalyzeResponceSerializer(analyzedFiles,many=True)
        return Response(serializer.data)
