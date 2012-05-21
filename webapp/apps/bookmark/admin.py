from django.contrib import admin
from bookmark.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bookmark, BookmarkAdmin)