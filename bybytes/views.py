from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from bybytes.models import DoubleFile


class DoubleFileView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(DoubleFile.objects.first().file_image)

class DoubleFileBytesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(DoubleFile.objects.first().bytes_file)