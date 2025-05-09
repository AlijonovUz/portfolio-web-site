from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
    path('portfolio/<slug:slug>/', ProjectDetailView.as_view(), name='detail'),
    path('portfolio/<slug:slug>/comment/', CommentView.as_view(), name='comment'),
]