from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.product,name='product'),
    path('category/<int:category_id>',views.product,name='productcategory'),
    path('<int:id>',views.productdetail,name='productdetail'),
]




