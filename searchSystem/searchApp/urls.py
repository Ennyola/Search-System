from django.urls import path,include
from . import views


app_name = "searchapp"

urlpatterns = [
    path("init-login/", views.init_login, name = "init-login"),
    path("sign_in/", views.login_page , name = "sign-in"),
    path("logout/", views.logout_view, name = "logout"),
    path("search_data/", views.search_bar , name = "search" )
]
