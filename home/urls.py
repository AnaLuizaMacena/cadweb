from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/', views.categoria, name="categoria" ),
    path('categoria/form', views.form_categoria, name="form_categoria" ),
    path('editar_categoria/<int:id>/', views.editar_categoria, name="editar_categoria" ),
    path('detalhes_categoria/<int:id>/', views.detalhes_categoria, name="detalhes_categoria" ),
    path('excluir_categoria/<int:id>/', views.excluir_categoria, name="excluir_categoria" ),
]