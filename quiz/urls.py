from django.urls import path

from . import views

urlpatterns = [
    path("", views.CategoriesView.as_view(), name="index"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("<slug:slug>/<slug:next_slug>/", views.TestDetailView.as_view(), name="test_detail"),
    path("<slug:slug>/<slug:next_slug>/result/", views.test_result, name="test_result"),
]
