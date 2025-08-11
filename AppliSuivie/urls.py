from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import AppliSuivie.views
#

app_name = "AppliSuivie"
#
urlpatterns = [
    path('',AppliSuivie.views.home, name='homepage'),
    path('alerts/',AppliSuivie.views.alerts,name='alert'),
    path('transactions/',AppliSuivie.views.transactions,name='transaction'),
        path('parametres/',AppliSuivie.views.settings,name='parametres'),

        path('previsions/',AppliSuivie.views.forecast,name='previsions'),
    path('rapports/',AppliSuivie.views.report,name='rapport'),

]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
