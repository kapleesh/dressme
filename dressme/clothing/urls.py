from django.conf.urls import url, include
from clothing.views import user_login, index, register, logout_view

urlpatterns = [
    url(r'^$', index),
    url(r'^user_login/$', user_login, name='user_login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout_view, name='logout_view')
]