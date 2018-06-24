from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='page_home'),
    url(r'^img1/$', views.page_1, name='page_1'),
    url(r'^img2/$', views.page_2, name='page_2'),
    url(r'^img3/$', views.page_3, name='page_3'),
    url(r'^img11/$', views.page_11, name='page_11'),
    url(r'^img12/$', views.page_12, name='page_12'),
    url(r'^img13/$', views.page_13, name='page_13'),
    url(r'^img21/$', views.page_21, name='page_21'),
    url(r'^img22/$', views.page_22, name='page_22'),
    url(r'^img23/$', views.page_23, name='page_23'),
    url(r'^img31/$', views.page_31, name='page_31'),
    url(r'^img32/$', views.page_32, name='page_32'),
    url(r'^img33/$', views.page_33, name='page_33'),
]
