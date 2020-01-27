from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def show_img(request, room_name=None):
    return render(request, 'viewimages/index.html')
