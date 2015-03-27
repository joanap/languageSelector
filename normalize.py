#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, codecs, re

def normalizeLine(line):
    normalizedLine = re.sub(ur"[<>]","",line)
    normalizedLine = re.sub(ur"([,;.?!:\"“”%()=€$£…])", ur" \1 ", normalizedLine)
    normalizedLine = re.sub(ur" +", r" ", normalizedLine)
    normalizedLine = re.sub(ur"^(.*)$", ur"<<\1>", normalizedLine)
    normalizedLine = re.sub(ur"(.) (>)$", ur"\1\2", normalizedLine)
    normalizedLine = normalizedLine.lower()
    return normalizedLine

def normalizeFile(inputFile, outputFile):
    for line in inputFile:
        outputFile.write(normalizeLine(line))

def main():
    f = codecs.open(sys.argv[1], "r", "utf-8")
    o = codecs.open(sys.argv[2], "w", "utf-8")

    normalizeFile(f, o)

    f.close()
    o.close()

if __name__ == "__main__":
    main()
