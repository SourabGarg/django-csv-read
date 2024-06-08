from csv_read.models import CSVUpload
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')

def result(request):
    print("-----------")
    csv_uploads = CSVUpload.objects.all()

    csv_files = []
    partial_path = "media/"
    for csv_upload in csv_uploads:
        if csv_upload.csv.name.endswith('.csv'):
            filename = csv_upload.csv.name
            csv_files.append(partial_path + filename)

    csv_file = csv_files[-1]
    data_file = pd.read_csv(csv_file, na_values='None')

    numeric_columns = data_file.select_dtypes(include='number').columns
    numeric_stats = data_file[numeric_columns].agg(['mean', 'median', 'std'])

    plt.figure()
    plt.scatter(data_file['Age'], data_file['Salary'])
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.title('Age vs Salary')

    plots_folder = "static"
    plot_path = plots_folder + "/age_vs_salary_plot.png"
    plt.savefig(plot_path)

    context = {'csv_files': csv_files,
               'numeric_stats': numeric_stats.to_dict(),
               'plot_path': plot_path}
    return render(request, "result/result.html", context)