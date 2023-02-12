from django.shortcuts import render, redirect
from .models import Report


# Create your views here.

def report(request):
    if request.method == "POST":
        if request.POST["btn1"] == "Submit":
            labName = request.POST['labID']
            date = request.POST['date']
            problem = request.POST['problem']
            if request.POST['creditCheck'] == "yes":
                type1 = "hardware"
            else:
                type1 = "software"
            data = Report(labID=labName, date=date, type=type1, problem=problem)
            data.save()
            return redirect("home")
    return render(request, 'forum/report/report.html')
