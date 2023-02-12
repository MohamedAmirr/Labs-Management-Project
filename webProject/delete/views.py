from django.shortcuts import render


# Create your views here.

def delete(request):
    return render(request, 'forum/update/delete/delete.html')
