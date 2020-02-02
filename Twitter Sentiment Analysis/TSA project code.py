# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:38:22 2019

@author: herna
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

#lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(word):
    count = 0
    output = strip_punctuation(word)
    for word in output.split():
        if word in positive_words:
            count += 1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(word):
    count = 0
    output = strip_punctuation(word)
    for word in output.split():
        if word in negative_words:
            count += 1
    return count

org_file = open("project_twitter_data.csv", 'r')
tweets = org_file.readlines()
header = tweets[0]

new_file = open("resulting_data.csv", 'w')
new_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
new_file.write("\n")
               
for tweet in tweets[1:]:
    value = tweet.strip().split(",")
    retweets = value [1]
    replies = value [2]
    pos_score = get_pos(tweet)
    neg_score = get_neg(tweet)
    net_score = pos_score - neg_score
    row_string = "{},{},{},{},{}".format(retweets, replies, pos_score, neg_score, net_score)
    new_file.write(row_string)
    new_file.write("\n")
new_file.close()
print(new_file)
