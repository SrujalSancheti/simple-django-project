from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path("signup/validate", views.signup_validate, name="signup_validate"),
    path('login', views.c_login, name="login"),
    path('login/send_otp', views.send_otp, name="send_otp"),
    path("login/validate", views.login_validate, name="login_validate"),
    path('search', views.search, name="search"),
    path('country/(?P<country_name>[\w|\W]+)', views.get_country_details, name="country_page"),
    path('logout', views.c_logout, name="logout"),
]
