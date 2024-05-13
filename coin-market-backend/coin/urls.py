from django.urls import path
from coin.views import *

urlpatterns = [
    path('receive-data', receive_data, name='receive_data'),
    path('get-coins-data', get_coins_data, name='get_coins_data'),
    path('', show_coins_data, name='show_coins_data'),
]
