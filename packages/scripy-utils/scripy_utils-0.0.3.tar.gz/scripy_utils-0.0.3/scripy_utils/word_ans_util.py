# -*- coding: utf-8 -*-
"""
@Time : 2023/12/16 15:05 
@项目：2-文本类
@File : word.by
@PRODUCT_NAME :PyCharm
"""
import jieba
import jieba.posseg as seg
import matplotlib
from matplotlib import pyplot as plt
# 下载 nltk_data
# https://www.nltk.org/nltk_data/
# 英文文本可以使用nltk库进行分词。可以使用nltk.tokenize中的word_tokenize()函
from snownlp import SnowNLP
from textblob import TextBlob
from wordcloud import WordCloud

matplotlib.use('TKAgg')
import pandas as pd
import numpy as np

# from googletrans import Translator
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class WordCloudUtil(object):
    def __init__(self, characters, font_path, cloud_output_path=None, mask_img_path=None):
        """
        :param characters: 输入文本
        :param font_path: 字体路径
        :param cloud_output_path: 词云输出路径
        :param img_path: 背景图片路径
        """
        self.font_path = font_path
        if mask_img_path is not None:
            self.mask = plt.imread(mask_img_path)
        else:
            self.mask = None
        self.cloud_output_path = cloud_output_path
        self.characters = characters
        #

    # 中文词云
    def create_wordcloud(self, **kwargs):
        self.words = jieba.lcut(self.characters)
        characters_s = ','.join(self.words)
        wordcloud1 = WordCloud(
            font_path=self.font_path,
            min_word_length=2,
            include_numbers=False,  # 是否将数字作为词。
            mask=self.mask,  # 背景图形,如果想根据图片绘制，则需要设置
            **kwargs
            # width=2000,  # 默认宽度
            # height=2000,  # 默认高度
            # margin=2,  # 边缘
            # ranks_only=None,
            # prefer_horizontal=0.9,
            # color_func=None,
            # max_words=200,  # 显示最多的词汇量
            # stopwords=None,  # 停止词设置，修正词云图时需要设置
            # random_state=None,
            # background_color='white',  # 背景颜色设置，可以为具体颜色，比如：white或者16进制数值。
            # font_step=1,
            # mode='RGB',
            # regexp=None,
            # collocations=True,
            # normalize_plurals=True,
            # contour_width=0,
            # colormap='viridis',  # matplotlib色图，可以更改名称进而更改整体风格
            # contour_color='Blues',
            # repeat=False,
            # scale=2,
            # min_font_size=10,
            # max_font_size=200
            # margin=词间距。
            # ranks_only=文档未说明。
            # prefer_horizontal=词语横排显示的概率(默认为90 %，则竖排显示概率为10 %)
            # # scale=比例尺，用于放大画布的尺寸。一般使用默认值。
            # color_func=颜色函数，一般不用。
            # max_words: 词云图中最多显示词的字数，设定一个值，可让那些出现次数极少的词不显示出来。
            # min_font_size: 字号最小值。
            # stopwords: 设置不想显示的词。
            # random_state=文档未说明。
            # background_color=词云图背景色，默认为黑色。可根据需要调整。
            # max_font_size=字号最大值。
            # font_step=字体的步长，一般使用默认。大于1的时候可提升运算速度，但匹配较差。
            # mode=当设置为"RGBA" 且background_color 设置为"None" 时可产生透明背景。
            # relative_scaling=词频对字体大小的影响度，一般使用默认。
            # regexp=正则表达式分割输入的字符。一般是先处理好才给到wordcloud，所以基本不用。
            # collocations=是否包含两个词的搭配，若使用了
            # generate_from_frequencies
            # 方法则忽略此参数。一般不用。
            # colormap=每个词对应的颜色，若设置了
            # color_func
            # 则忽略此参数。
            # normalize_plurals=是否移除英文复数单词末尾的s ，比如可将word和words视同为一个词，并将词频算到word头上。如果使用了
            # generate_from_frequencies
            # 方法则忽略此参数。
            # contour_width=如果
            # mask
            # 有设置，且
            # contour_width > 0，将会绘制
            # mask
            # 轮廓。
            # contour_color=mask
            # 轮廓的颜色，默认为黑色。
            # repeat=当词不足以满足设定的
            # max_words
            # 时，是否重复词或短语以使词云图上的词数量达到
            # max_words
            # min_word_length=设置一个词包含的最少字母数量。
            # collocation_threshold=界定英文中的
            # bigrams，对于中文不适用。
        ).generate(characters_s)
        wordcloud1.to_file(f"{self.cloud_output_path}")

    # 英文词云
    def create_wordcloud_english(self, **kwargs):
        characters_s = ','.join(self.characters.split())
        wordcloud1 = WordCloud(
            font_path=self.font_path,
            min_word_length=2,
            include_numbers=False,  # 是否将数字作为词。
            mask=self.mask,  # 背景图形,如果想根据图片绘制，则需要设置
            **kwargs
        ).generate(characters_s)
        wordcloud1.to_file(f"{self.cloud_output_path}")

    # 中文词频统计
    def word_frequency(self, frequency_path, stopWords: list = [], ):
        self.words = jieba.lcut(self.characters)
        wordsDict = {}  # 新建字典用于储存词及词频
        for word in self.words:
            if len(word) == 1:  # 单个的字符不作为词放入字典
                continue
            else:
                wordsDict.setdefault(word, 0)  # 设置词的初始出现次数为0
                wordsDict[word] += 1  # 对于重复出现的词，每出现一次，次数增加1
        # stopWords = ["公司", "行业", "000", "用于", "情况", "方面", "一种", "要求", "对于", "进行", "一般", "212", "实现", "处理", "通过", "投入",
        #              "随着"]
        for word in stopWords:
            if word in wordsDict:
                del wordsDict[word]  # 删除对应的词
        wordsDict_seq = sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)  # 按字典的值降序排序
        df = pd.DataFrame(wordsDict_seq, columns=['词', '次数'])
        df.to_excel(f"{frequency_path}", index=False)  # 存为Excel时去掉index索引列
        return wordsDict_seq

    # 英文词频统计
    def word_frequency_english(self, frequency_path):
        data_split = self.characters.split()  # 以空格切割英文字母
        wordsDict = {}  # 定义字典
        for word in data_split:
            if word not in wordsDict:  # 读取的单词不在词典内
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1  # 读取的单词在词典内
        wordsDict_seq = sorted(wordsDict.items(), key=lambda x: x[1], reverse=True)  # 按字典的值降序排序
        df = pd.DataFrame(wordsDict_seq, columns=['词', '次数'])
        df.to_excel(f"{frequency_path}", index=False)  # 存为Excel时去掉index索引列
        return wordsDict_seq

    # 中文情感分析
    def SnowNLP_ans(self, frequency_path):
        words_ans = []
        analysis_words = [(word.word, word.flag) for word in seg.cut(self.characters)]
        keywords = [x for x in analysis_words if x[1] in ['a', 'd', 'v']]
        keywords = [x[0] for x in keywords]
        pos_num = 0
        neg_num = 0
        for word in keywords:
            sl = SnowNLP(word)
            sentiments = sl.sentiments
            if sentiments > 0.5:
                pos_num = pos_num + 1
                word_sentiments = "正面"
            else:
                # Adding 1 to the value of `neg_num`.
                neg_num = neg_num + 1
                word_sentiments = "负面"
            words_ans.append(
                [word, sentiments, word_sentiments
                 ]
            )
        print('正面情绪关键词数量：{}'.format(pos_num))
        print('负面情绪关键词数量：{}'.format(neg_num))
        print('正面情绪所占比例：{}'.format(pos_num / (pos_num + neg_num)))
        df = pd.DataFrame(words_ans, columns=['词', '情感值', '情绪'])
        df.to_excel(f"{frequency_path}", index=False)  # 存为Excel时去掉index索引列
        return words_ans, pos_num, neg_num

    def SnowNLP_ans_Phrases(self, frequency_path):
        words_ans = []
        # analysis_words = [(word.word, word.flag) for word in seg.cut(self.characters)]
        # print(analysis_words)
        # keywords = [x for x in analysis_words if x[1] in ['a', 'd', 'v']]
        # keywords = [x[0] for x in keywords]
        pos_num = 0
        neg_num = 0
        print(self.characters)
        for word in self.characters:
            print(word)
            sl = SnowNLP(word)
            sentiments = sl.sentiments
            if sentiments > 0.5:
                # sentiments = 1
                pos_num = pos_num + 1
                word_sentiments = "正面"
            else:
                # Adding 1 to the value of `neg_num`.
                neg_num = neg_num + 1
                word_sentiments = "负面"
                # sentiments  =  0
            words_ans.append(
                [sentiments, word,  # word_sentiments
                 ]
            )
        print('正面情绪关键词数量：{}'.format(pos_num))
        print('负面情绪关键词数量：{}'.format(neg_num))
        print('正面情绪所占比例：{}'.format(pos_num / (pos_num + neg_num)))
        df = pd.DataFrame(words_ans, columns=['label', 'review',  # '情绪'
                                              ])
        df.to_csv(f"{frequency_path}", index=False)  # 存为Excel时去掉index索引列
        return words_ans, pos_num, neg_num

    # 英文情感分析
    def TextBlob_ans_english(self, frequency_path):
        words_ans = []
        pos_num = 0
        neg_num = 0
        neuter_num = 0
        blob = TextBlob(self.characters)
        sentences = blob.sentences
        for sentence in sentences:
            print(sentence.sentiment.polarity)
            sentiment = blob.sentiment.polarity
            if sentiment > 0:
                result = '正面'
                pos_num += 1
            elif sentiment < 0:
                result = '负面'
                neg_num += 1
            else:
                result = '中性'
                neuter_num += 1
            words_ans.append(['词', sentiment, result])
        print('正面情绪关键词数量：{}'.format(pos_num))
        print('负面情绪关键词数量：{}'.format(neg_num))
        print('正面情绪所占比例：{}'.format(pos_num / (pos_num + neg_num)))
        df = pd.DataFrame(words_ans, columns=['词', '情感值', '情绪'])
        df.to_excel(f"{frequency_path}", index=False)  # 存为Excel时去掉index索引列
        return words_ans, pos_num, neg_num, neuter_num

    # 情感分直方图
    def emotion_plt(self, words_ans):
        bins = np.arange(0, 1.1, 0.1)
        plt.hist([i[0] for i in words_ans], bins, color='#4F94CD', alpha=0.9)
        plt.xlim(0, 1)
        plt.xlabel('情感分')
        plt.ylabel('数量')
        plt.title('情感分直方图')
        plt.show()

    def emotion_proportion_plt(self, pos_num, neg_num, neuter_num=None):
        pie_labels = ['positive', 'negative']
        dat1 = [pos_num, neg_num]
        if neuter_num:
            dat1.append(neuter_num)
            pie_labels.append("neuter")
        plt.pie([pos_num, neg_num], labels=pie_labels, autopct='%1.2f%%', shadow=True)
        plt.show()
