# -*- coding: utf-8 -*-

# https://www.nltk.org/book/ch01.html

# pip install nltk nicht vergessen!
#import PyPDF2

import nltk, re, pprint

from nltk import word_tokenize
from nltk import tokenize
#from nltk import corpus
from nltk.tokenize import RegexpTokenizer

from collections import Counter

def test():
    text = "Dies ist ein Test."
    tokens = word_tokenize(text)

    print(tokens[:10])
    
class Nltkanalysis(object):
    def __init__(self,
                 text):
        self.text = text
        self.tokenizedtext = self.__textTokenize(self.text)
        self.tags = self.__textTags(self.tokenizedtext)
        self.wordCount = 0
        self.mostCommonWord = []        
        self.adjectivecount = 0
        self.nouncount = 0
        self.verbcount = 0
        
    """
    def lexicalDispersionPlot(self, ??):
        .dispersion_plot(
    """
    def runAnalysis(self, measurements):
        
        list = [int(d) for d in str(measurements)]
        list.reverse()
        for index, item in enumerate(list):
            if(list[index] == 1):
                if(index == 0):
                    print('Analyse 1')
                    self.wordCount = len(self.tokenizedtext)
                elif(index == 1):
                    print('Analyse 2')
                    self.mostCommonWord = self.__mostCommonWord(self.tokenizedtext)
                elif(index == 2):
                    print('Analyse 3')
                    #self.tags = self.__textTags(self.tokenizedtext)
                    self.adjectivecount = self.__adjectiveCount(self.tags)
                elif(index == 3):
                    print('Analyse 4')
                    self.nouncount = self.__nounCount(self.tags)
                elif(index == 4):
                    print('Analyse 5')
                    self.verbcount = self.__verbCount(self.tags)
                    #print(self.adjectivecount)
                    #print(self.nouncount)
                    #print(self.verbcount)
                #elif(index == 3):
                    
                else:
                    pass

    def runApiAnalysis(self, measurements):

        list = [int(d) for d in str(measurements)]
        list.reverse()
        for index, item in enumerate(list):
            if (list[index] == 1):
                if (index == 0):
                    print('Analyse 1')
                    self.wordCount = len(self.tokenizedtext)
                elif (index == 1):
                    print('Analyse 2')
                    self.mostCommonWord = self.__mostCommonWord(self.tokenizedtext)
                elif (index == 2):
                    print('Analyse 3')
                    # self.tags = self.__textTags(self.tokenizedtext)
                    self.adjectivecount = self.__adjectiveCount(self.tags)
                elif (index == 3):
                    print('Analyse 4')
                    self.nouncount = self.__nounCount(self.tags)
                elif (index == 4):
                    print('Analyse 5')
                    self.verbcount = self.__verbCount(self.tags)
                    # print(self.adjectivecount)
                    # print(self.nouncount)
                    # print(self.verbcount)
                # elif(index == 3):

                else:
                    pass

    """        
    def __dispersionPlot(self, tokenizedtext):
        ...
        
    def __lexicalDiversity(self, tokenizedtext):
        ld = ...
        
        
    long words
    >>> V = set(text1)
>>> long_words = [w for w in V if len(w) > 15]
>>> sorted(long_words)

    collocations()
    

    """    
    def __createTextCollection(self, textlist):
        # bsp mytexts = TextCollection([text1, text2, text3])
        textcollection = nltk.TextCollection(textlist)
        return textcollection
    
    # term frequency
    def __tf(self, term, textcollection):
        return textcollection.tf()
    
    # inter document frequency
    def __idf(self, term, textcollection):
        return textcollection.idf(term, textcollection)
    
    def __tfIdf(self, textcollection):
        return textcollection.tf_idf()
    
    
    def __mostCommonWord(self, tokenizedtext):
        fd = nltk.FreqDist(tokenizedtext)
        mostCommonWord = fd.most_common(1)
        return mostCommonWord
    
    def __adjectiveCount(self, counts):
        # JJ: Adjective; JJR: Adjective, comparative; JJS: Adjective, superlative; 
        adjectivecount = counts['JJ'] + counts['JJR'] + counts['JJR']
        return adjectivecount
    
    def __nounCount(self, counts):
        # NN: Noun, singular or mass; NNS: Noun, plural; NNP: Proper noun, singular; NNPS: Proper noun, plural
        nouncount = counts['NN'] + counts['NNS'] + counts['NNP'] + counts['NNPS']
        return nouncount
    
    def __verbCount(self, counts):
        # VBP: Verb, base present; VB: Verb, base form; VBD: Verb, past tense; VBG: Verb, gerund or present participle; VBZ: Verb, present 3sg
        verbcount = counts['VBP'] + counts['VB'] + counts['VBD'] + counts['VBG'] + counts['VBN'] + counts['VBZ']
        return verbcount
    
    def __textTags(self, tokenizedtext):
        taggedtext = nltk.pos_tag(tokenizedtext)
        counts = Counter(tag for word,tag in taggedtext)
        print(counts)
        return counts
        # Counter({'DT': 2, 'NN': 2, 'VB': 1})
        

    def __textTokenize(self, text):
        # regexp to remove punctuation
        tokenizer = RegexpTokenizer(r'\w+')
        tokenizedtext = tokenizer.tokenize(text)
        return tokenizedtext



