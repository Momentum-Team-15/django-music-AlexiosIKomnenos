from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music import views

# urlpatterns = [
#         path('', views.album_directory, name='base'),
# ]

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)