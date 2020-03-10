from django.urls import include, path
from .views.HomeView import HomeView
from .views.ProductView import ProductView
from .views.CategoryView import CategoryView
from .views.OrderView import OrderView
from .views.UserView import UserView
from .views.ProviderView import ProviderView

home = HomeView()
product = ProductView()
category = CategoryView()
order = OrderView()
user = UserView()
provider = ProviderView()

urlpatterns = [
    path('', home.index),
    path('products', product.index),
    path('product/new', product.form),
    path('product/<int:id>', product.form),
    path('product/<int:id>/delete', product.delete),

    path('categories', category.index),
    path('category/new', category.form),
    path('category/<int:id>', category.form),
    path('category/<int:id>/delete', category.delete),

    path('orders', order.index),
    path('order/new', order.form),
    path('order/<int:id>', order.form),
    path('order/<int:id>/delete', order.delete),

    path('users', user.index),
    path('user/new', user.form),
    path('user/<int:id>', user.form),
    path('user/<int:id>/delete', user.delete),


    path('providers', provider.index),
    path('provider/new', provider.form),
    path('provider/<int:id>', provider.form),
    path('provider/<int:id>/delete', provider.delete),
]