#!/usr/bin/python
# -*- coding: utf-8 -*-
import nGramCount as n
import normalize as norm
import os, codecs
import numpy
import sys
import re

def loadCount(path):
    f = codecs.open(path, "r", "utf-8")
    count = dict()

    for line in f:
        lst = line.rstrip().split('\t')
        count[lst[0]] = lst[1]

    return count

def probability(sentenceTrigrams, bigrams, trigrams):
    prob = 1
    for trigram in sentenceTrigrams:
        if not trigram in trigrams:
            return 0
        else:
            num = numpy.float64(trigrams[trigram]) 

        if not trigram[:-1] in bigrams:
            return 0
        else:
            den = numpy.float64(bigrams[trigram[:-1]])
            prob += numpy.log10(numpy.divide(num , den) )

    return prob

def probabilityAdd1(sentenceTrigrams, bigrams, trigrams):
    prob = numpy.float64(1)
    v = numpy.float64(len(bigrams) + 1)
    for trigram in sentenceTrigrams:
        if not trigram in trigrams:
            num = 1
        else:
            num = numpy.float64(trigrams[trigram]) + 1

        if not trigram[:-1] in bigrams:
            den = v
        else:
            den = numpy.float64(bigrams[trigram[:-1]]) + v
        
        prob += numpy.log10( numpy.divide(num , den) ) 


    return prob

def calcLanguageProbability(normalizedSentence, language):
    trigrams = dict()
    bigrams = dict()
    sentenceTrigrams = n.countNGramsLine(dict(), normalizedSentence, 3).keys()

    for subdir, dirs, files in os.walk(language):
        for file in files:
            path = os.path.join(subdir, file)
            if ".trigrama" in file:
                trigrams = loadCount(path)
            if ".bigrama" in file:
                bigrams = loadCount(path)


    return (probability(sentenceTrigrams, bigrams, trigrams) ,
            probabilityAdd1(sentenceTrigrams, bigrams, trigrams) )


def printResults(result):
    for k, v in sorted(result.iteritems(), key=lambda (k,v): (-v,k)):
        print "\tResult - Language: {0} Value: {1}".format(k,v)

def main():
    sentence  = sys.argv[1].decode("utf-8")
    languages = ['pt', 'en', 'es', 'fr', 'it']
    normalizedSentence = norm.normalizeLine(sentence)

    probabilities = dict()
    probabilitiesNormalized = dict()

    for language in languages:
        result = calcLanguageProbability(normalizedSentence, language)
        probabilities[language] = result[0]
        probabilitiesNormalized[language] = result[1]

    print "Probabilities for sentence: \n\t", sentence.encode("utf-8"), "\n"
    print "Normalized Form: \n\t", normalizedSentence.encode("utf-8")
    print "\nProbabilities:"
    printResults( probabilities )
    print "Probabilities with smoothing:"
    printResults( probabilitiesNormalized )


if __name__ == "__main__":
    main()
