from django.urls import path
from .views import FlagListView, FlagUpdateView, GenerateFlagView, KeywordListCreateView,LoadContentView, MatchTestView, ScanView

urlpatterns = [
    path('keywords/', KeywordListCreateView.as_view(), name='keywords'),
    path('load-content/', LoadContentView.as_view()),
    path('test-matching/', MatchTestView.as_view()),
    path('generate-flags/', GenerateFlagView.as_view()),
    path('scan/', ScanView.as_view()),
    path('flags/', FlagListView.as_view()),
    path('flags/<int:pk>/', FlagUpdateView.as_view()),
]