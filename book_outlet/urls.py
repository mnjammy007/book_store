from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.book_detail_by_id, name="book-detail-by-id"),
    path("<slug:slug>", views.book_detail, name="book-detail"),
]
