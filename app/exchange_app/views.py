from django.shortcuts import render
import requests


def exchange(request):

    responce = requests.get(
        url='https://v6.exchangerate-api.com/v6/16cf980d64fbad705c1cb61d/latest/USD').json()
    currencies = responce.get('conversion_rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }

        return render(request=request, template_name='exchange_app\index.html', context=context)

    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        if not from_amount:
            from_amount = 0

        converted_amount = round(
            (currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request=request, template_name='exchange_app\index.html', context=context)
