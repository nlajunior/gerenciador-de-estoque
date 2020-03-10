from django.urls import include, path
from .views.HomeView import HomeView
from .views.ProductView import ProductView
from .views.CategoryView import CategoryView
from .views.OrderView import OrderView
from .views.UserView import UserView
from .views.ProviderView import ProviderView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings

home = HomeView()
product = ProductView()
category = CategoryView()
order = OrderView()
user = UserView()
provider = ProviderView()

urlpatterns = [
    path('dashboard', login_required(home.index)),

    path('', user.login),
    path('login', user.login),
    path('logout', login_required(user.logout)),

    path('products', login_required(product.index)),
    path('product/new', login_required(product.form)),
    path('product/<int:id>', login_required(product.form)),
    path('product/<int:id>/delete', login_required(product.delete)),

    path('categories', login_required(category.index)),
    path('category/new', login_required(category.form)),
    path('category/<int:id>', login_required(category.form)),
    path('category/<int:id>/delete', login_required(category.delete)),

    path('orders', login_required(order.index)),
    path('order/new', login_required(order.form)),
    path('order/<int:id>', login_required(order.form)),
    path('order/<int:id>/delete', login_required(order.delete)),

    path('users', login_required(user.index)),
    path('user/new', login_required(user.form)),
    path('user/<int:id>', login_required(user.form)),
    path('user/<int:id>/delete', login_required(user.delete)),


    path('providers', login_required(provider.index)),
    path('provider/new', login_required(provider.form)),
    path('provider/<int:id>', login_required(provider.form)),
    path('provider/<int:id>/delete', login_required(provider.delete)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)