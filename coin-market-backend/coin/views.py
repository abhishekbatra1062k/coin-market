from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from coin.models import CoinData

def send_data_to_django(data):
    for item in data:
        coin, created = CoinData.objects.get_or_create(name=item['name'])
        coin.price = item['price']
        coin.rank = item['rank']
        coin.symbol = item['symbol']
        coin.one_hour_change = item['one_hour_change']
        coin.twenty_four_hour_change = item['twenty_four_hour_change']
        coin.seven_day_change = item['seven_day_change']
        coin.market_cap = item['market_cap']
        coin.volume_24h = item['volume_24h']
        coin.circulating_supply = item['circulating_supply']
        coin.save()

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        send_data_to_django(data) 
        return JsonResponse({'message': 'Data received successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def get_coins_data(request):
    if request.method == 'GET':
        coins = CoinData.objects.all().values()
        return JsonResponse({'data': list(coins)}, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

@csrf_exempt
def show_coins_data(request):
    if request.method == 'GET':
        coins = CoinData.objects.all().values()
        return render(request, 'coin_data.html', {'coins': coins})
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)