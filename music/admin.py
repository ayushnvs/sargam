from django.contrib import admin
from .models import Singer, Author, Album, Song

admin.site.register(Singer)
admin.site.register(Author)
admin.site.register(Album)
admin.site.register(Song)
