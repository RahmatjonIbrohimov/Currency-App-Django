from os import path
from pathlib import Path

import requests
import json

from django.shortcuts import render

# Create your views here.



def data():
    fpath = path.join(Path(__file__).resolve().parent, 'templates/currency.json')
    with open(fpath, "r") as file:
        currency_data = json.loads(file.read())
    return currency_data

def home(request):
    # print(request.method)
    if request.method == "POST" :
        sum = request.POST.get('sum')
        fromm = request.POST.get("currency_from").lower()
        to = request.POST.get("currency_to").lower()

        x = requests.get(
            f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{fromm}/{to}.json").json()
        res = float(sum) * float(x[to])

        save = {'res': round(res, 4), 'cfrom': fromm.upper(), 'to': to.upper(), 'sum':sum,  'data': data}

        return render(request, 'currency/index.html', save)

    else:
        x = requests.get(
                    f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/uzs.json").json()
        return render(request, 'currency/index.html', {'data': data()})
