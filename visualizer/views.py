from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie

from visualizer.forms import DataForm
from visualizer.models import Data
from django.shortcuts import render, redirect
from django.urls import reverse
import json

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['data_form'] = DataForm()
        context['customers'] = 10
        data_set = Data.objects.all()
        states = list()
        years = set()
        for data in data_set:
            if data.state not in states:
                states.append('%s' % data.state)

        for data in data_set:
            if data.year not in years:
                years.add('%s' % data.year)

        print(states)
        print(years)

        series = list()
        for year in years:
            data = list()
            for state in states:
                one = Data.objects.filter(year = year).filter(state = state)
                if len(one) > 0:
                    for val in one:
                        data.append(val.population)
                else:
                    data.append(0)
            sery = {
                'name': year,
                'data': data
            }
            series.append(sery)

        print(series)
        chart = {
            'chart': {'type': 'column'},
            'title': {'text': 'Historical US Population by State'},
            'xAxis': {'categories': states},
            'series': series
        }
        context['chart'] = json.dumps(chart)

        return render(request, 'home.html', context)


# def get_data(request, *args, **kwargs):
#     data = {
#         "sales": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data) # http response
#
#
# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         d = Data.objects.all()
#         data = [one.dump() for one in d]
#         response_text = json.dumps({"data": data})
#         print(response_text)
#         # labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
#         # default_items = [23, 2, 3, 12, 2]
#         # data = {
#         #         "labels": labels,
#         #         "default": default_items,
#         # }
#         return Response(response_text)

@ensure_csrf_cookie
def add_data(request):
    context = {}

    new_data = Data()
    data_form = DataForm(request.POST, instance=new_data)

    if not data_form.is_valid():
        context['data_form'] = data_form
    else:
        new_data.year = data_form.cleaned_data['year']
        new_data.state = data_form.cleaned_data['state']
        new_data.population = data_form.cleaned_data['population']
        data_form.save()
        context['data_form'] = DataForm()

    return redirect(reverse('home'))