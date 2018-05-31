from django.contrib import admin
from django.conf.urls import url,include
from . import views
from djgeojson.views import GeoJSONLayerView
from multigtfs.models import Stop
from osmapp.models import Node
from gtfs.models import GTFSForm
from django.views.generic import TemplateView
from .views import FormView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',include('gtfs.urls'),name='gtfs'),
    url(r'^gtfs/',include('gtfs.urls')),
    url(r'^nodedata/', GeoJSONLayerView.as_view(model=Node, properties=('id')), name="nodedata"),

]
