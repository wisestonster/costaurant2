from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = {"date": today}
    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = dict()
    if food == "chicken":
        context["name"] = "코딩에 빠진 닭"
        context["description"] = "주머니가 가벼운 당신의 마음까지 생각한 가격 !"
        context["price"] = 10000
        context["img_path"] = "foods/images/chicken.jpg"
    else:
        raise Http404("이런 음식은 없다구요 !")
    return render(request, 'foods/detail.html', context=context)