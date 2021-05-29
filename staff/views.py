from django.shortcuts import render
from .models import StorageStaff


# Create your views here.
def list_staff(request):
    staffs = StorageStaff.objects.all()
    return render(request, 'staffs.html', {'staffs': staffs})
