from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import FileData
from django.contrib import messages
from tablib import Dataset
from django.db.models import Count


def upload(request):
    if request.method == "POST":
        dataset = Dataset()
        new_data = request.FILES["myfile"]

        if not new_data.name.endswith("xlsx"):
            messages.info(request, "Please check your file format!")
            return render(request, "fileupload.html")

        FileData.objects.all().delete()

        imported_data = dataset.load(new_data.read(), format="xlsx")
        for data in imported_data:
            value = FileData(
                date=data[0],
                accno=data[1],
                state=data[2],
                pin=data[3],
                dpd=data[4],
            )
            value.save()

    return redirect("/")


def home(request):
    result = (
        FileData.objects.values("state", "dpd")
        .annotate(dpd_count=Count("dpd"))
        .order_by("state")
    )

    return render(request, "fileupload.html", {"result": result})
