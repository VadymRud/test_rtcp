from django.contrib import admin
from import_export import resources
from .models import Rtu, BiDesc, AiDesc

admin.site.register(Rtu)
admin.site.register(BiDesc)
admin.site.register(AiDesc)


class RtuResource(resources.ModelResource):
    class Meta:
        model = Rtu


class BiDescResource(resources.ModelResource):
    class Meta:
        model = BiDesc


class AiDescResource(resources.ModelResource):
    class Meta:
        model = AiDesc
