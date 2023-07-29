from django.shortcuts import render
from .models import Kitob
from django.views.generic import DetailView
# Create your views here.
def HomePageView(request):
	return render(request, 'home.html')

def kitoblar(request):
    query = request.GET.get('sorov')
    addition = "So'rov bo'yicha natijalar"
    if query:
        results = Kitob.objects.filter(nomi__contains=query, muallif__contains=query)
    else:
        results = Kitob.objects.filter().order_by()
        query = ""
    
    context = {
        'results': results,
        'query': query,
        'addition': addition
    }
    return render(request, 'kitoblar.html', context)
def dokonlar(request):
	return render(request, 'dokonlar.html')
def about(request):
	return render(request, 'about.html')
class DetailPageView(DetailView):
	model = Kitob
	template_name = 'detail.html'