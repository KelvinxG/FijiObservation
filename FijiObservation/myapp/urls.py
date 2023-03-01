from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import IndexView,AboutAuthorView,ContactView,VisualizerView,SolutionView


urlpatterns= [

    path('',IndexView.as_view(),name='index'),
    path('visualizer/',VisualizerView.as_view(),name='visualizer'),
    path('aboutauthor/',AboutAuthorView.as_view(),name='aboutauthor'),
    path('solutions/',SolutionView.as_view(),name='solutions'),
    path('contact/',ContactView.as_view(),name='contact'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)