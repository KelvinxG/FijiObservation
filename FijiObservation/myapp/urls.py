from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns= [

    path('',views.index,name='index'),
    path('visualizer/',views.visualizer,name='visualizer'),
    path('aboutauthor/',views.aboutauthor,name='aboutauthor'),
    path('solutions/',views.solutions,name='solutions'),
    path('contact/',views.contact,name='contact'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)