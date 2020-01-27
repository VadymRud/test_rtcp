from django.contrib import admin
from django.urls import path
from viewimages.views import show_img

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_camera', show_img)

]
