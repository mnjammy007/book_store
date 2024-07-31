from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from .models import Book
from django.urls import reverse
from django.db.models import Avg


def index(request):
    books = Book.objects.all().order_by("-rating")
    avg_rating = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": books.count,
            "average_rating": avg_rating,
        },
    )


def book_detail_by_id(request, id):
    book_slug = get_object_or_404(Book, pk=id).slug
    redirect_path = reverse("book-detail", args=[book_slug])
    return HttpResponseRedirect(redirect_path)


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestseller,
        },
    )
