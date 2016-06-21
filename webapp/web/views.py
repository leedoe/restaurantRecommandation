from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    output="<html><head><title></title></head><body><h1>TEST</h1></body></html>"
    return HttpResponse(output)
