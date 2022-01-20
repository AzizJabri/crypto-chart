from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .getters import *

# Create your views here.
def ApiView(request,**kwargs):
    interval = kwargs['interval']
    match interval:
        case 'daily':
            data = get_price_daily()
        case 'weekly':
            data = get_price_weekly()
        case 'monthly':
            data = get_price_monthly()
        case 'yearly':
            data = get_price_yearly()
        case _:
            data = [[],[],[]]
    return JsonResponse({
        'labels': data[0] ,
        'priceBtc' : data[1],
        'priceEth' : data[2]
    })

class HomeView(View):
    def get(self,request,*arg,**kwarg):
        return render(request,'chart/charts.html')

def page_not_found(request,exception):
    return render(request,'404.html')