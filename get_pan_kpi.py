import csv
import os

csvfiles = os.listdir("csv")
print csvfiles
pan_kpi_list = []

for csvf in csvfiles:
    if len(csvf.split(".")) < 0 or cmp(csvf.split(".")[1], "csv"):
	continue
    if len(csvf.split(".")[0]) < 1:
	continue
    print csvf
    benchmark = csvf.split(".")[0]

    pan_kpi = [benchmark]
    csvfile = file("csv/" + csvf, "rb")
    reader = csv.reader(csvfile)
    for line in reader:
        for metric in line:
            if not cmp(benchmark, metric.split(".")[0]):
                pan_kpi.append(metric)
        break
    csvfile.close()
    pan_kpi_list.append(pan_kpi)

csvfile = file('pan-kpi.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerows(pan_kpi_list)
csvfile.close()
