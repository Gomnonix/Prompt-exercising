from django.urls import path

from .views import FitplanListView, FitplanPostView

urlpatterns = [
    path("", FitplanListView.as_view(), name="fitplan_list"),
    path("post", FitplanPostView.as_view(), name="fitplan_post"),
]
