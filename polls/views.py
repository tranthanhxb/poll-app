from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    myname = "Trần Thanh"
    taisan = ["Điện thoại", "Máy tính", "Máy bay", "Nhiều tiền"]
    context = {"name": myname, "taisan": taisan}
    return render(request, "polls/index.html", context)

