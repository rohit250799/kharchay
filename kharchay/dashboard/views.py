from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def dashboard(request):
    #return HttpResponse("This is a dashboard")
    return render(request, 'dashboard/dashboard.html')