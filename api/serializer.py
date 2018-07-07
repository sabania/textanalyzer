from rest_framework import serializers
from api.models import AnalyzeRequest
from pdfanalyzer.models import UploadFile

class AnalyzeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyzeRequest
        fields = ('__all__')


class AnalyzeResponceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = '__all__'

