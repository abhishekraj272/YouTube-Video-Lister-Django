from django.shortcuts import render, redirect
from rest_framework import pagination, generics
from .models import VideoDetails
from .serializer import VideoDetailSerializers

def index(request):
    return redirect('/dashboard')

def dashboard(request):
    return render(request, 'lister/index.html')

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DashboardDatAPI(generics.ListAPIView):
    queryset = VideoDetails.objects.all()
    serializer_class = VideoDetailSerializers
    pagination_class = StandardResultsSetPagination

print('555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555')