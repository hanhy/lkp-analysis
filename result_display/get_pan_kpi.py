import csv
import os

csvfiles = os.listdir("csv")
pan_kpi_list = []

for csv in csvfiles:
    benchmark = csv.split("/")[1].split(".")[0]

    pan_kpi = [benchmark]
    csvfile = file(csv_file, "rb")
    reader = csv.reader(csvfile)
    for line in reader:
        for metric in line:
            if not cmp(benchmark, metric.aplit(".")[0]):
                pan_kpi.append(metric)
        break
    csvfile.close()
    pan_kpi_list.append(pan_kpi)

csvfile = file('pan-kpi.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerows(pan_kpi_list)
csvfile.close()
