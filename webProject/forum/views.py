from django.http import HttpResponse
from django.shortcuts import render
from add.models import LabInfo


# Create your views here.

def forum(request):
    return render(request, 'forum/forum.html')


def getLabInfo(request):
    data = list(LabInfo.objects.all())
    string = ""
    for item in data:
        string += '<a '
        string += 'href="/forum/update/">'
        string += item.labName
        string += '</a>'

    return HttpResponse(string)
