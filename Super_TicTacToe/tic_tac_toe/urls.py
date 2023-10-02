from django.urls import path

from Super_TicTacToe.tic_tac_toe.views import home_view, pvp_view, super_pvp_view

urlpatterns = [
    path('', home_view.home, name='home'),
    path('pvp/', pvp_view.pvp, name='pvp'),
    path('super_pvp/', super_pvp_view.super_pvp, name='super_pvp')
]