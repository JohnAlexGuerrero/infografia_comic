from django.contrib import admin

from comic.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','image','created_at')

