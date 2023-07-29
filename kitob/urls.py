from django.urls import path
from .views import HomePageView, DetailPageView, kitoblar, dokonlar, about

urlpatterns = [
	path('', HomePageView, name="home"),
    path('kitoblar/', kitoblar, name="kitoblar"),
    path('dokonlar/', dokonlar, name="dokonlar"),
	path('qoshimcha-malumot/', about, name="about"),
	path('<slug:slug>/', DetailPageView.as_view(), name="detail")
] 