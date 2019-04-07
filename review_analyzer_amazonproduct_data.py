# Takes Reviews from json data and analyze it into no of positive,negative and neutral ones

import json
from textblob import TextBlob
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
def percentage(part,whole):
    return 100*float(part)/float(whole)

data = []
reviewlist=[]
review=[]
pos=0
neg=0
neutral=0
polarity=0
analysis="Good"
rev=[]
review=[]
with open("C://rdata//data.json","r") as f:
    for line in f:
        data.append(json.loads(line))
    #print(data)
    for reviews in data:
        reviewlist=reviews['reviewText']
        review.append(reviewlist)
    for x in review:
        analysis=TextBlob(x)
        polarity += analysis.sentiment.polarity

        if(analysis.sentiment.polarity == 0):
             neutral+= 1
        elif(analysis.sentiment.polarity <0.00):
             neg += 1
        elif(analysis.sentiment.polarity>0.00):
             pos+=1
#print(len(review))
#print(review)
noofsearchitems=len(review)
pos=percentage(pos,noofsearchitems)

neutral=percentage(neg,noofsearchitems)
neutral=percentage(neutral,noofsearchitems)
print("Maximum Reaction of people after analyzing  " +str(noofsearchitems) +" reviews")

if(polarity==0):
 print("Neutral")
elif(polarity<0):
 print("Negative")
elif(polarity>0):
 print("Positive")

labels = ['Positive['+str(pos)+'%]','Neutral [' +str(neutral) + '%]', 'Negative[' +str(neg) +'%]']
sizes=[pos,neutral,neg]
colors=['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
