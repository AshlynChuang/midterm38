from django.contrib import admin
from mysite.models import Book

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')

admin.site.register(Book, PostAdmin)