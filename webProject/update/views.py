from django.shortcuts import render


# Create your views here.
def update(request):
    return render(request, 'forum/update/update.html')
