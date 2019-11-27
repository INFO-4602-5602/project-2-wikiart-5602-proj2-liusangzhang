# Paintings evoking positive emotions were liked more, in general.
# Paintings evoking no emotion were the least liked paintings.

# --> Positive: Paintings that bring to mind certain positive emotions such as <love>
#       were liked much more than paintings that bring to mind other positive emotions such as <humility>.
# --> Negative: Paintings bringing to mind <regret>, <arrogance>, and <sadness> were liked much more than
#       paintings bringing to mind <disgust>, <anger>, or <fear>.

# import pandas as pd
import csv

# f = pd.read_csv("WikiArtClean.csv", delimiter=",")
datalist = []
newdatalist = []
with open("WikiArtClean_new.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # print(row)
        datalist.append(row[:])
        newdatalist.append(row[:])

newdatalist[0].extend(["POS", "NEG", "MIX"])

positive_emotions = ["Gratitude", "Happiness", "Humility", "Love", "Optimism", "Trust"]
negative_emotions = ["Anger", "Arrogance", "Disgust", "Fear", "Pessimism", "Regret", "Sadness", "Shame"]
mixed_emotions = ["Agreeableness", "Anticipation", "Disagreeableness", "Shyness", "Surprise", "Neutral"]

# print(len(positive_emotions+negative_emotions+mixed_emotions))
emotions = ["Agreeableness", "Anger", "Anticipation", "Arrogance",
            "Disagreeableness", "Disgust", "Fear", "Gratitude",
            "Happiness", "Humility", "Love", "Optimism", "Pessimism",
            "Regret", "Sadness", "Shame", "Shyness", "Surprise",
            "Trust", "Neutral"]

emotion_id_dict = {}
for i, emotion in enumerate(emotions):
    emotion_id_dict[emotion] = i - len(emotions)

# print(emotion_id_dict)

# print(len(datalist))
# print(datalist[1])

# print(set(positive_emotions + negative_emotions + mixed_emotions) - set(emotions))

# print(len(newdatalist[0]))
# print()
# print(len(newdatalist[1]))

for row, rownew in zip(datalist[1:], newdatalist[1:]):
    pos_sum = 0
    neg_sum = 0
    mix_sum = 0
    for emotion in positive_emotions:
        pos_sum += float(row[emotion_id_dict[emotion]])
    rownew.append(round(pos_sum, 2))

    for emotion in negative_emotions:
        neg_sum += float(row[emotion_id_dict[emotion]])
    rownew.append(round(neg_sum, 2))

    for emotion in mixed_emotions:
        mix_sum += float(row[emotion_id_dict[emotion]])
    rownew.append(round(mix_sum, 2))

# print([datalist[0]])
# print()
# print(newdatalist[0])
#
# print([datalist[-1]])
# print()
# print(newdatalist[-1])

# print(len(datalist))
# print()
# print(len(newdatalist))

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# https://matplotlib.org/3.1.1/tutorials/introductory/customizing.html

# plt.style.use('Solarize_Light2')
# plt.style.use('fivethirtyeight')
plt.style.use('grayscale')
# plt.xkcd()

def avg(listval):
    return round(sum(listval)/len(listval), 2)

def plotByStyle():
    styles = ["Renaissance Art", "Post Renaissance Art", "Modern Art", "Contemporary Art"]
    # https://matplotlib.org/3.1.1/api/markers_api.html#module-matplotlib.markers
    markers = ["o", "h", "s", "D"] # circle, square, hexagon1, diamond

    yRenaissance = []
    yPostRenaissance = []
    yModern = []
    yContemporary = []

    xposRenaissance = []
    xposPostRenaissance = []
    xposModern = []
    xposContemporary = []

    xnegRenaissance = []
    xnegPostRenaissance = []
    xnegModern = []
    xnegContemporary = []

    xmixRenaissance = []
    xmixPostRenaissance = []
    xmixModern = []
    xmixContemporary = []

    for row in newdatalist[1:]:
        if row[0] == styles[0]:
            yRenaissance.append(float(row[10]))
            xposRenaissance.append(float(row[-3]))
            xnegRenaissance.append(float(row[-2]))
            xmixRenaissance.append(float(row[-1]))

        if row[0] == styles[1]:
            yPostRenaissance.append(float(row[10]))
            xposPostRenaissance.append(float(row[-3]))
            xnegPostRenaissance.append(float(row[-2]))
            xmixPostRenaissance.append(float(row[-1]))

        if row[0] == styles[2]:
            yModern.append(float(row[10]))
            xposModern.append(float(row[-3]))
            xnegModern.append(float(row[-2]))
            xmixModern.append(float(row[-1]))

        if row[0] == styles[3]:
            yContemporary.append(float(row[10]))
            xposContemporary.append(float(row[-3]))
            xnegContemporary.append(float(row[-2]))
            xmixContemporary.append(float(row[-1]))

    yval = [avg(yRenaissance), avg(yPostRenaissance), avg(yModern), avg(yContemporary)]
    xpos = [avg(xposRenaissance), avg(xposPostRenaissance), avg(xposModern), avg(xposContemporary)]
    xneg = [avg(xnegRenaissance), avg(xnegPostRenaissance), avg(xnegModern), avg(xnegContemporary)]
    xmix = [avg(xmixRenaissance), avg(xmixPostRenaissance), avg(xmixModern), avg(xmixContemporary)]
    xall = [avg(xposRenaissance + xnegRenaissance + xmixRenaissance),
            avg(xposPostRenaissance + xnegPostRenaissance + xmixPostRenaissance),
            avg(xposModern + xnegModern + xmixModern),
            avg(xposContemporary + xnegContemporary + xmixContemporary)]

    print("yval", yval)
    print("xpos", xpos)
    print("xneg", xneg)
    print("xmix", xmix)
    print("xall", xall)

    # plt.scatter(xpos, yval, label="avg postive emotions")
    # https://matplotlib.org/3.1.0/gallery/color/named_colors.html

    for x, y, m in zip(xall, yval, markers):
        # plt.scatter(x, y, marker=m, edgecolor="black", c="yellow", s=100, label="avg all emotions")
        plt.scatter(y, x, marker=m, c="yellow", s=100, label="avg all emotions")
        # txt = '(' + str(x) + ', ' + str(y) + ')'
        # plt.annotate(txt, (x, y), rotation=0, color="black")

    for x, y, m in zip(xneg, yval, markers):
        plt.scatter(y, x, marker=m, edgecolor="black", c="darkorange", s=100, label="avg negative emotions")
        # txt = '(' + str(x) + ', ' + str(y) + ')'
        # plt.annotate(txt, (x, y), rotation=0, color="darkorange", horizontalalignment="right", verticalalignment="top")
    # plt.scatter(xneg, yval, label="avg negative emotions")
    # for i, txt in enumerate(styles):
    #     plt.annotate(txt, (xneg[i], yval[i]))

    for x, y, m in zip(xmix, yval, markers):
        plt.scatter(y, x, marker=m, edgecolor="black", c="#0E4C92", s=100, label="avg mixed emotions")
        # txt = '(' + str(x) + ', ' + str(y) + ')'
        # plt.annotate(txt, (x, y), rotation=0, color="lightsteelblue", horizontalalignment="center", verticalalignment="bottom")
    # plt.scatter(xmix, yval, label="avg mixed emotions")
    # for i, txt in enumerate(styles):
    #     plt.annotate(txt, (xmix[i], yval[i]))

    for x, y, m in zip(xpos, yval, markers):
        plt.scatter(y, x, marker=m, edgecolor="black", c="#4CBB17", s=100, label="avg postive emotions")
        # txt = '(' + str(x) + ', ' + str(y) + ')'
        # plt.annotate(txt, (x, y), rotation=0, color="limegreen", horizontalalignment="left", verticalalignment="top") # https://matplotlib.org/3.1.1/api/text_api.html#matplotlib.text.Text
                                                 # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.annotate.html
    # for i, txt in enumerate(styles):
    #     plt.annotate(txt, (xpos[i], yval[i]))

    # plt.xlabel("Emotion Score")
    # plt.ylabel("Mean Rating")

    plt.xlabel("Mean Rating")
    plt.ylabel("Emotion Votes")

    plt.title("Mean Rating by Art Style and Average Votes by Emotion Type")

    # plt.legend()
    # https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/custom_legends.html
    # "Renaissance Art", "Post Renaissance Art", "Modern Art", "Contemporary Art"
    # "o", "s", "h", "D"
    legend_elements = [Line2D([0], [0], color='w', marker='o', markeredgecolor='black', markersize=10, label='Renaissance'),
                       Line2D([0], [0], color='w', marker='h', markeredgecolor='black', markersize=10, label='Post Renaissance'),
                       Line2D([0], [0], color='w', marker='s', markeredgecolor='black', markersize=10, label='Modern'),
                       Line2D([0], [0], color='w', marker='D', markeredgecolor='black', markersize=10, label='Contemporary'),
                       Line2D([0], [0], color='w', marker='s', markerfacecolor='#4CBB17', markersize=10, label='Positve emotion avg'),
                       Line2D([0], [0], color='w', marker='s', markerfacecolor='darkorange', markersize=10, label='Negative emotion avg'),
                       Line2D([0], [0], color='w', marker='s', markerfacecolor='#0E4C92', markersize=10, label='Mixed emotion avg'),
                       Line2D([0], [0], color='w', marker='s', markerfacecolor='yellow', markersize=10, label='All emotion avg')]

    # legend_elements = [Line2D([0], [0], color='w', marker='o', markeredgecolor='black', label='Renaissance'),
    #                     Line2D([0], [0], color='w', marker='h', markeredgecolor='black', label='Post Renaissance'),
    #                     Line2D([0], [0], color='w', marker='s', markeredgecolor='black', label='Modern'),
    #                     Line2D([0], [0], color='w', marker='D', markeredgecolor='black', label='Contemporary'),
    #                     Line2D([0], [0], color='w', marker='s', markerfacecolor='limegreen', label='Positve emotion avg'),
    #                     Line2D([0], [0], color='w', marker='s', markerfacecolor='darkorange', label='Negative emotion avg'),
    #                     Line2D([0], [0], color='w', marker='s', markerfacecolor='lightsteelblue', label='Mixed emotion avg'),
    #                     Line2D([0], [0], color='w', marker='s', markerfacecolor='black', label='All emotion avg')]

    plt.legend(handles=legend_elements)
    # plt.legend()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # plt.gca().spines['left'].set_visible(False)
    # plt.gca().spines['bottom'].set_visible(False)

    plt.tight_layout()

    plt.savefig("emotionByType.png", dpi=300)
    # plt.show()
    plt.close()

plotByStyle()


def plotByIndividual():
    yval = []
    xpos = []
    xneg = []
    xmix = []

    for row in newdatalist[1:]:
        yval.append(row[10])
        xpos.append(row[-3])
        xneg.append(row[-2])
        xmix.append(row[-1])
        # print(row[10], '\t', row[-3:])

    # plt.scatter(yval, xpos)
    # plt.scatter(yval, xneg)
    # plt.scatter(yval, xmix)

    plt.plot(yval, xpos)
    # plt.plot(yval, xneg)
    # plt.plot(yval, xmix)

    plt.show()

# plotByIndividual()

############################################

# print(newdatalist[0])
# print()
# print(newdatalist[1])
# print(yval[0], xpos[0], xneg[0], xmix[0])







