from django.conf.urls import url
from pay import views
app_name = 'pay'
urlpatterns = [
    url(r'^index/$',views.index,name = 'index'),
    url(r'^getpay/$',views.getpay,name = 'getpay'),
]