from django.urls import path

from boxes.views import SelectBoxView

urlpatterns = [
    path("select-box/", SelectBoxView.as_view(), name="select-box"),
]
