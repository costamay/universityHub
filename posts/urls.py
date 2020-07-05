from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projectList, name='post-list'),
    path('post/<id>/', views.singleproject, name='post-detail'),
    path('create/', views.post_project, name='post-create'),
    path('post/<id>/update/', views.post_update, name='post_update'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)