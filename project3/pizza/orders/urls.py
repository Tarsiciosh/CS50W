from django.urls import path
from . import views # . current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("menu", views.menu, name="menu"),
    path("add_item", views.add_item, name="add_item"),
    path("confirm_order", views.confirm_order, name="confirm_order")
]