styles = ["Renaissance Art", "Post Renaissance Art", "Modern Art", "Contemporary Art"]

renaissance = ["Early Renaissance", "High Renaissance", "Northern Renaissance"]
postRenaissance = ["Baroque", "Neoclassicism", "Realism", "Rococo", "Romanticism"]
modern = ["Abstract Art", "Abstract Expressionism", "Art Informel", "Color Field Painting", "Cubism",
            "Expressionism", "Impressionism", "Lyrical Abstraction", "Magic Realism", "Neo-Expressionism",
            "Pop Art", "Post-Impressionism", "Surrealism"]
contemporary = ["Minimalism"]

categories = renaissance + postRenaissance + modern + contemporary

catStyleDict = {}
for c in renaissance:
    catStyleDict[c] = "Renaissance Art"
for c in postRenaissance:
    catStyleDict[c] = "Post Renaissance Art"
for c in modern:
    catStyleDict[c] = "Modern Art"
for c in contemporary:
    catStyleDict[c] = "Contemporary Art"

import csv
from collections import defaultdict

datalist = []
with open("WikiArtClean_new.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        datalist.append(row[:])

catRateDict = defaultdict(list)
catStyleDict = defaultdict(list)
for row in datalist[1:]:
    style = row[0]
    cat = row[1]
    # cats = set(row[1].strip().split(','))
    meanrate = float(row[10])
    # for cat in categories:
    #     if cat in cats:
    #         catRateDict[cat].append(meanrate)
    catRateDict[cat].append(meanrate)
    catStyleDict[cat].append(style)

# print(catRateDict.keys())

with open("style_category_meanRating.csv", mode="w") as csvwrite:
    fw = csv.writer(csvwrite, delimiter=",")
    fw.writerow(['Style', 'Category', 'Mean Rating'])
    for k, v in catRateDict.items():
        fw.writerow([catStyleDict[k][0], k, round(sum(v)/len(v), 2)])



