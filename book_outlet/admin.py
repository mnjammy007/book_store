from django.contrib import admin
from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author")
    list_filter = ("author", "rating")
    # search_fields = ("title", "rating")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "postal_code")


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
