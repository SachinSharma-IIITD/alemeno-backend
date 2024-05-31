# analyzer/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UrineStripImage
from .serializers import UrineStripImageSerializer
from .utils import analyze_image_colors
from django.shortcuts import render

def index(request):
    """
    Render the index page with the upload form.
    """
    return render(request, 'index.html')

class AnalyzeImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request to analyze the uploaded urine strip image.
        """
        file_serializer = UrineStripImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_instance = file_serializer.save()
            image_path = file_instance.image.path
            print(f'\nImage path: {image_path}\n')
            colors = analyze_image_colors(image_path)

            debug_response = {
                'colors': colors,
                'color_values': [colors]
            }
            return Response(colors, status=200)
        else:
            return Response(file_serializer.errors, status=400)
