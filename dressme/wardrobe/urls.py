from django.conf.urls import url
from . import views

app_name = 'wardrobe'
urlpatterns = [
        url(r'^register/$', views.RegisterFormView.as_view(), name = 'register'),
]
