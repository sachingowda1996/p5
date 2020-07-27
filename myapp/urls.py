from django.urls import path
from myapp import views

urlpatterns = [
    path('child/',views.child,name='child'),
    path('base/',views.base,name='base'),
]
