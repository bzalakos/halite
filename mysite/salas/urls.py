"""This is the list of all of the URL Patterns the site will accept. Maps the url to the View."""
from django.conf.urls import url

from . import views

app_name = 'salas'
urlpatterns = [
    url(r'^$', views.ProductsListView.as_view(), name='products'),
    url(r'^products/(?P<pk>\d+)$', views.ProductView.as_view(), name='product'),
    url(r'^coupons/$', views.CouponsListView.as_view(), name='coupons'),
    url(r'^tags/$', views.TagsListView.as_view(), name='tags'),
    url(r'^purchases/$', views.PurchasesListView.as_view(), name='purchases'),
    url(r'^purchases/(?P<pk>\d+)/$', views.PurchaseView.as_view(), name='purchase'),
    url(r'^account/$', views.AccountView.as_view(), name='account'),
    url(r'^users/$', views.UsersListView.as_view(), name='users'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
]
