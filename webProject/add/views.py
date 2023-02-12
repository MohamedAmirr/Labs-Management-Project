from django.shortcuts import render
from .models import LabInfo


# Create your views here.

def add(request):
    if request.method == "POST":
        _labName = request.POST.get('labName')
        _labID = request.POST.get('labID')
        _buildingNumber = request.POST.get('buildingNumber')
        _floorNumber = request.POST.get('floorNumber')
        _numOfPcs = request.POST.get('numOfPcs')
        _capacity = request.POST.get('capacity')
        _numOfChairs = request.POST.get('numOfChairs')
        data = LabInfo(labName=_labName, labID=_labID,
                       buildingNumber=_buildingNumber,
                       floorNumber=_floorNumber,
                       numOfPcs=_numOfPcs,
                       capacity=_capacity,
                       numOfChairs=_numOfChairs)

        data.save()
    return render(request, 'forum/add/add.html')
