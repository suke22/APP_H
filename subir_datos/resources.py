from import_export import resources
from .models import Dato

class DatoResource(resources.ModelResource):
    class Meta:
        model = Dato
