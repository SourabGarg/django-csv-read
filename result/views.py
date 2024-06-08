from django.shortcuts import render
from csv_read.models import CSVUpload


def result(request):
    print("_----------")
    csv_uploads = CSVUpload.objects.all()

    csv_files = []
    partial_path = "csv_read/media/"
    for csv_upload in csv_uploads:
        if csv_upload.csv.name.endswith('.svg'):
            filename = csv_upload.csv.name
            csv_files.append(partial_path + filename)

    context = {'csv_files': csv_files}
    return render(request, "result/result.html", context)

