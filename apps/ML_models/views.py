from rest_framework import views
from rest_framework.response import Response
from apps.ML_models.serializers import ModelDataSerializer
from apps.ML_models.utility import get_firebase_data
import pickle
import numpy as np

with open('apps/ML_models/saved_models/random_forest_model.pkl', 'rb') as file:
    random_forest = pickle.load(file)


class ModelAPIView(views.APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        response = get_firebase_data()
        data = response[0]

        data_serializer = ModelDataSerializer(data=data)
        data_serializer.is_valid(raise_exception=True)

        data = [float(value) for value in list(data_serializer.validated_data.values())]
        x = np.array([data])

        prediction = random_forest.predict(x)

        return Response(prediction)

    def post(self, request):
        data_serializer = ModelDataSerializer(data=request.data)
        data_serializer.is_valid(raise_exception=True)

        # np.array([[feature1, feature2, ..., featureN]])
        data = [float(value) for value in list(data_serializer.validated_data.values())]
        x = np.array([data])

        prediction = random_forest.predict(x)

        return Response(prediction)
