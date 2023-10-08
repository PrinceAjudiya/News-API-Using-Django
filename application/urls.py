from . import views
from django.urls import path

urlpatterns = [
    path("",views.index),
    path("tesla/",views.tesla),
    path("tesla-output",views.tesla_output),
    path("business/",views.business),
    path("business-output",views.business_output),
]
