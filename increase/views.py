from django.shortcuts import render
from .models import Count

# Create your views here.
def count(request):
    if Count.objects.exists():
        count = Count.objects.get(id=1)
        count.count += 1
        count.save()
    else:
        count = Count(id=1)
        count.count += 1
        count.save()
    return render(request, 'count.html', {
    'count': count.count,
    })
    