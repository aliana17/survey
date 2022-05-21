from django.urls import URLPattern, path
from . import views

app_name = "survey"

urlpatterns = [
    path("", views.home, name="home"),
    path("questions/<int:cust_id>/<int:id>", views.handler, name="handler"),
    path("questions", views.start, name="start"),
    path("close", views.close, name="close"),
]
