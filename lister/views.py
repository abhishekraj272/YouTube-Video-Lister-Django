from django.shortcuts import render, redirect
from rest_framework import pagination, generics
from .models import VideoDetails
from .serializer import VideoDetailSerializers
import asyncio, threading
from .utils import loop_in_thread

def index(request):
    return redirect('/dashboard')

def dashboard(request):
    return render(request, 'lister/index.html')

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class VideoDetailsAPI(generics.ListAPIView):
    """
    Fetches video details from DataBase in paginated way.
    """
    queryset = VideoDetails.objects.all()
    serializer_class = VideoDetailSerializers
    pagination_class = StandardResultsSetPagination

# Puts the get_data_from_youtube fucntion in background
loop = asyncio.get_event_loop()
t = threading.Thread(target=loop_in_thread, args=(loop,))
t.start()