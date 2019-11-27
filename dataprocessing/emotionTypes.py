positive_emotions = ["Gratitude", "Happiness", "Humility", "Love", "Optimism", "Trust"]
negative_emotions = ["Anger", "Arrogance", "Disgust", "Fear", "Pessimism", "Regret", "Sadness", "Shame"]
mixed_emotions = ["Agreeableness", "Anticipation", "Disagreeableness", "Shyness", "Surprise", "Neutral"]

emotions = ["Agreeableness", "Anger", "Anticipation", "Arrogance",
            "Disagreeableness", "Disgust", "Fear", "Gratitude",
            "Happiness", "Humility", "Love", "Optimism", "Pessimism",
            "Regret", "Sadness", "Shame", "Shyness", "Surprise",
            "Trust", "Neutral"]

emotiontypedict = {}
for e in positive_emotions:
    emotiontypedict[e] = "Positive"
for e in negative_emotions:
    emotiontypedict[e] = "Negative"
for e in mixed_emotions:
    emotiontypedict[e] = "Other or Mixed"

import csv
from collections import defaultdict

datalist = []
with open("WikiArtClean_new.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        datalist.append(row[:])

emotioncountdict = defaultdict(int)
emotionMeanScoreDict = defaultdict(list)

for row in datalist[1:]:
    emotionMeanScoreDict["Agreeableness"].append(float(row[-20]))
    emotionMeanScoreDict["Anger"].append(float(row[-19]))
    emotionMeanScoreDict["Anticipation"].append(float(row[-18]))
    emotionMeanScoreDict["Arrogance"].append(float(row[-17]))
    emotionMeanScoreDict["Disagreeableness"].append(float(row[-16]))
    emotionMeanScoreDict["Disgust"].append(float(row[-15]))
    emotionMeanScoreDict["Fear"].append(float(row[-14]))
    emotionMeanScoreDict["Gratitude"].append(float(row[-13]))
    emotionMeanScoreDict["Happiness"].append(float(row[-12]))
    emotionMeanScoreDict["Humility"].append(float(row[-11]))
    emotionMeanScoreDict["Love"].append(float(row[-10]))
    emotionMeanScoreDict["Optimism"].append(float(row[-9]))
    emotionMeanScoreDict["Pessimism"].append(float(row[-8]))
    emotionMeanScoreDict["Regret"].append(float(row[-7]))
    emotionMeanScoreDict["Sadness"].append(float(row[-6]))
    emotionMeanScoreDict["Shame"].append(float(row[-5]))
    emotionMeanScoreDict["Shyness"].append(float(row[-4]))
    emotionMeanScoreDict["Surprise"].append(float(row[-3]))
    emotionMeanScoreDict["Trust"].append(float(row[-2]))
    emotionMeanScoreDict["Neutral"].append(float(row[-1]))

    if float(row[-20]) != 0:
        emotioncountdict["Agreeableness"] += 1
    if float(row[-19]) != 0:
        emotioncountdict["Anger"] += 1
    if float(row[-18]) != 0:
        emotioncountdict["Anticipation"] += 1
    if float(row[-17]) != 0:
        emotioncountdict["Arrogance"] += 1
    if float(row[-16]) != 0:
        emotioncountdict["Disagreeableness"] += 1
    if float(row[-15]) != 0:
        emotioncountdict["Disgust"] += 1
    if float(row[-14]) != 0:
        emotioncountdict["Fear"] += 1
    if float(row[-13]) != 0:
        emotioncountdict["Gratitude"] += 1
    if float(row[-12]) != 0:
        emotioncountdict["Happiness"] += 1
    if float(row[-11]) != 0:
        emotioncountdict["Humility"] += 1
    if float(row[-10]) != 0:
        emotioncountdict["Love"] += 1
    if float(row[-9]) != 0:
        emotioncountdict["Optimism"] += 1
    if float(row[-8]) != 0:
        emotioncountdict["Pessimism"] += 1
    if float(row[-7]) != 0:
        emotioncountdict["Regret"] += 1
    if float(row[-6]) != 0:
        emotioncountdict["Sadness"] += 1
    if float(row[-5]) != 0:
        emotioncountdict["Shame"] += 1
    if float(row[-4]) != 0:
        emotioncountdict["Shyness"] += 1
    if float(row[-3]) != 0:
        emotioncountdict["Surprise"] += 1
    if float(row[-2]) != 0:
        emotioncountdict["Trust"] += 1
    if float(row[-1]) != 0:
        emotioncountdict["Neutral"] += 1

# print(emotioncountdict)

with open("emotion_type_count.csv", mode="w") as csvwrite:
    fw = csv.writer(csvwrite, delimiter=",")
    fw.writerow(['Type', 'Emotion', 'Count'])
    for e in emotions:
        fw.writerow([emotiontypedict[e], e, emotioncountdict[e]])

with open("emotion_type_meanScore.csv", mode="w") as csvwrite:
    fw = csv.writer(csvwrite, delimiter=",")
    fw.writerow(['Type', 'Emotion', 'Mean Score'])
    for e in emotions:
        fw.writerow([emotiontypedict[e], e, round(sum(emotionMeanScoreDict[e])/len(emotionMeanScoreDict[e]), 4)])



