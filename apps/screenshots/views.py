from rest_framework import mixins
from rest_framework import generics

from .serializers import *


# Create your views here.

class ScreenshotsList(generics.ListCreateAPIView):
    queryset = Screenshots.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ScreenshotCreateSerializer
        else:
            return ScreenshotsSerializer


class ScreenshotDetails(generics.RetrieveAPIView):
    queryset = Screenshots.objects.all()
    serializer_class = ScreenshotInfoSerializer
