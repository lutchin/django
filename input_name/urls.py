from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'input'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.results, name='results'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)