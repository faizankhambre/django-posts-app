from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts, name='posts'),
    path('new-post/', views.new_post, name='new_post'),
    path('<slug:slug>', views.post_page, name='post_page'),
]

# Serve media files even when DEBUG = False
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)