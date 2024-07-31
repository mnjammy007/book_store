from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")
    list_filter = ("author", "rating")
    # search_fields = ("title", "rating")


admin.site.register(Book, BookAdmin)
