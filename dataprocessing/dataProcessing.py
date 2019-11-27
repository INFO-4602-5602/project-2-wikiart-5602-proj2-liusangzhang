import csv
from collections import defaultdict

datalist = []
with open("WikiArtClean.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        datalist.append(row[:])

with open("WikiArtClean_new.csv", mode="w") as csvwrite:
    fw = csv.writer(csvwrite)
    fw.writerow(datalist[0])
    for row in datalist[1:]:
        styles = row[0].strip().split(',')
        if len(styles) > 1:
            print(styles)
        for style in styles:
            fw.writerow([style]+row[1:])
            
# The Categories for the 8 entries with more two Styles were manually splitted.



