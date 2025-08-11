from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import AppliSuivie.views
#

app_name = "Appli_suivie_entreprise"
#
urlpatterns = [
    path('',AppliSuivie.views.home, name='homepage'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
