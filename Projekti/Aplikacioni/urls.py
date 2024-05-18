from django.urls import path
from.import views


urlpatterns=[
    path("", views.navbar, name="navbar"),
    path("about/" , views.about , name="about"),
    path("blog/<id>" , views.blog , name="blog"),
    path("contact/" , views.contact , name="contact"),
    path("shop/<id>" , views.shop , name="shop"),
    path("register/" , views.register , name="register"),
    path('logout/', views.logout_view, name='logout'),
    path("login/" , views.LoginForm , name="login")
]
