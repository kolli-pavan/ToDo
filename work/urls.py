from django.urls import path
from . import views

urlpatterns=[
   
    path('',views.index, name='index'),
    path('add',views.add, name='adder'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('updater/<int:id>',views.updater,name='updater'),
]