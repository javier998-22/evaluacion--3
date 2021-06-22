from django.urls import path
from .views import home, form_libro, form_mod_libro, form_del_libro 

urlpatterns = [
    path('',home,name="home"),
    path('form-libro', form_libro,name="form_libro"),
    path('form-del-libro', form_del_libro, name="form_del_libro"),
]
