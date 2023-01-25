from django.urls import path
from .views import home, fotos, somos, taller, ayaka, kazuha, cerdo, zenit, nezu, drak, rana, koro, lu, colors, clientes, eliminar, crear, modificar, pro, addpro
urlpatterns=[
    path('', home, name="home"),
    path('fotos/', fotos, name="fotos"),
    path('somos/', somos, name="somos"),
    path('taller/', taller, name="taller"),
    path('ayaka/', ayaka, name="ayaka"),
    path('kazuha/', kazuha, name="kazuha"),
    path('cerdo/', cerdo, name="cerdo"),
    path('zenit/', zenit, name="zenit"),
    path('nezu/', nezu, name="nezu"),
    path('drak/', drak, name="drak"),
    path('rana/', rana, name="rana"),
    path('koro/', koro, name="koro"),
    path('lu/', lu, name="lu"),
    path('colors/', colors, name="colors"),
    path('clientes/', clientes, name="clientes"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('crear/',crear, name="crear"),
    path('modificar/<id>', modificar, name="modificar"),
    path('pro/', pro, name="pro"),
    path('addpro/', addpro, name="addpro"),
]