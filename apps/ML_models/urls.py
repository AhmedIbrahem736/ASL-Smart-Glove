from django.urls import path
from apps.ML_models.views import ModelAPIView


urlpatterns = [
    path('predict/', ModelAPIView.as_view()),
]
