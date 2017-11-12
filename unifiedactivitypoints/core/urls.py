from django.conf.urls import url
from . import views

urlpatterns =[
    url('^$',views.home,name="home"),
    url('^add-activity-points/$', views.add_activity_points, name="add_activity_points"),
]
