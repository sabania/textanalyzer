from django.urls import path

from . import views

urlpatterns = [
    path('analyze/', views.AnalyzeRequestAPIView.as_view(), name='analyze')
]