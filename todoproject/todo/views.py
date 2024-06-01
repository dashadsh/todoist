from django.shortcuts import render

# Create your views here.

# -------- NEW STUFF -------------------
from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# needed??

def index(request):
    return render(request, 'index.html')
# -------- NEW STUFF -------------------
