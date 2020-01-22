from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path
from viewimages.views import show_img
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', show_img, name='index')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
