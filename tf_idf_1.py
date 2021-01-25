# -*- coding: utf-8 -*-

# print("/".join(jieba.lcut(txt)))  # 精简模式，返回一个列表类型的结果
# print("/".join(jieba.lcut(txt, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定
# print("/".join(jieba.lcut_for_search(txt)))     # 搜索引擎模式


import math
import re
import jieba

txt1 = open("part1 共青团中央.json", "r", encoding='utf-8').read()
words1 = jieba.lcut_for_search(txt1)  # 使用jieba中的搜索引擎模式对3份文本进行分词
txt2 = open("part1 人民日报.json", "r", encoding='utf-8').read()
words2 = jieba.lcut_for_search(txt2)
txt3 = open("part1 央视新闻.json", "r", encoding='utf-8').read()
words3 = jieba.lcut_for_search(txt3)

s = open("stopwords.txt", encoding='utf-8', errors="ignore")  # 拉取停词表
chinese_stop = {}
for word in s:
    word = word.strip()
    chinese_stop[word] = 1
s.close()

counts = {}  # 通过键值对的形式存储词语及其出现的次数
tfs = {}  # 通过键值对的形式存储词语及其TF值
lines = {}  # 通过键值对的形式存储词语及其出现的行数
idfs = {}  # 通过键值对的形式存储词语及其IDF值
tf_idfs = {}  # 通过键值对的形式存储词语及其TF-IDF值
tf_idf_sums = {}  # 通过键值对的形式存储心态词及其对应的情绪词的TF-IDF值之和
frequencies = {}  # 通过键值对的形式存储心态词及其频率

wordCount = 0  # 总词数
for word in words1:
    if word not in chinese_stop.keys():  # 不考虑停词表中的词
        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加1
        wordCount += 1  # 总词数也加1
for word in words2:
    if word not in chinese_stop.keys():
        counts[word] = counts.get(word, 0) + 1
        wordCount += 1
for word in words3:
    if word not in chinese_stop.keys():
        counts[word] = counts.get(word, 0) + 1
        wordCount += 1

items = list(counts.items())
for i in range(len(counts)):  # 计算每个词语的TF值
    word, count = items[i]
    tfs[word] = count / wordCount

lineCount = 0  # 总行数
for line in open("part1 共青团中央.json", "r", encoding='utf-8'):
    lineCount += 1  # 总行数加1
    for i in range(len(counts)):
        word, count = items[i]
        if word in line:
            lines[word] = lines.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的行数加1
for line in open("part1 央视新闻.json", "r", encoding='utf-8'):
    lineCount += 1
    for i in range(len(counts)):
        word, count = items[i]
        if word in line:
            lines[word] = lines.get(word, 0) + 1
for line in open("part1 人民日报.json", "r", encoding='utf-8'):
    lineCount += 1
    for i in range(len(counts)):
        word, count = items[i]
        if word in line:
            lines[word] = lines.get(word, 0) + 1

for i in range(len(counts)):
    word3, line = items[i]
    idfs[word3] = math.log10(lineCount / line)  # 计算每个词语的IDF值

items2 = list(tfs.items())
items3 = list(idfs.items())
for i in range(len(counts)):
    word2, tf = items2[i]
    word3, idf = items3[i]
    tf_idfs[word2] = tf * idf  # 计算每个词语的TF-IDF值

items4 = list(tf_idfs.items())
for i in range(len(tf_idfs)):
    word4, tf_idf = items4[i]
    for line in open("心态词典.txt", "r", encoding='utf-8'):
        if word4 in line:
            line = re.sub('\n', '', line)
            lineList = line.split("\t")
            # 计算可映射到每个心态词的情绪词的TF-IDF值之和
            tf_idf_sums[lineList[2]] = lines.get(lineList[2], 0) + tf_idf

items5 = list(tf_idf_sums.items())
tf_idfCount = 0  # 所有情绪词的TF-IDF值之和
for i in range(len(tf_idf_sums)):
    feeling, tf_idf_sum = items5[i]
    tf_idfCount += tf_idf_sum

for i in range(len(tf_idf_sums)):
    feeling, tf_idf_sum = items5[i]
    frequencies[feeling] = round(tf_idf_sum / tf_idfCount, 5)  # 计算每个心态词的频率

items6 = list(frequencies.items())
items6.sort(key=lambda x: x[1], reverse=True)  # 根据心态词的频率进行从大到小的排序

for i in range(len(frequencies)):
    feeling, frequency = items6[i]
    print("{0:^5} {1:.5}%".format(feeling, frequency * 100))
