from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categoria/', views.categoria, name="categoria" ),
    path('categoria/form', views.form_categoria, name="form_categoria" ),
    path('editar_categoria/<int:id>/', views.editar_categoria, name="editar_categoria" ),
    path('detalhes_categoria/<int:id>/', views.detalhes_categoria, name="detalhes_categoria" ),
    path('excluir_categoria/<int:id>/', views.excluir_categoria, name="excluir_categoria" ),

#####################################CLIENTE#######################################################
    path('cliente/', views.cliente, name="cliente" ),
    path('cliente/form', views.form_cliente, name="form_cliente" ),
    path('editar_cliente/<int:id>/', views.editar_cliente, name="editar_cliente" ),
    path('detalhes_cliente/<int:id>/', views.detalhes_cliente, name="detalhes_cliente" ),
    path('excluir_cliente/<int:id>/', views.excluir_cliente, name="excluir_cliente" ),

#####################################PRODUTO################################################
    path('produto/', views.produto, name="produto" ),
    path('produto/form', views.form_produto, name="form_produto" ),
    path('editar_produto/<int:id>/', views.editar_produto, name="editar_produto" ),
    path('detalhes_produto/<int:id>/', views.detalhes_produto, name="detalhes_produto" ),
    path('excluir_produto/<int:id>/', views.excluir_produto, name="excluir_produto" ),
    path('ajustar_estoque/<int:id>/', views.ajustar_estoque, name="ajustar_estoque" ),

###############################################teste#############################
    path('teste1/', views.teste1, name='teste1'),
    path('teste2/', views.teste2, name='teste2'),
    path('teste3/', views.teste3, name='teste3'),
    path('buscar_dados/<str:app_modelo>/', views.buscar_dados, name='buscar_dados'),

#####################################PEDIDO################################################
    path('pedido/lista', views.pedido, name='pedido'),
    path('pedido/novo_pedido/<int:id>', views.novo_pedido, name='novo_pedido'),
    path('detalhes_pedido/<int:id>', views.detalhes_pedido, name='detalhes_pedido'),
    path('remover_pedido/<int:id>/', views.remover_pedido, name='remover_pedido'),
    path('remover_item_pedido/<int:id>/', views.remover_item_pedido, name='remover_item_pedido'),
    path('editar_item_pedido/<int:id>/', views.editar_item_pedido, name='editar_item_pedido'),
    path('form_pagamento/<int:id>/', views.form_pagamento, name='form_pagamento'),    
    path('remover_pagamento/<int:id>/', views.remover_pagamento, name='remover_pagamento'),
    path('notafiscal/<int:pedido_id>/', views.notafiscal, name='notafiscal'),
]