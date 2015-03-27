import sys, codecs

# Counts the number of n grams in a file
def countNGrams(f, n):
    nGramDict = dict()

    for line in f:
        nGramDict = countNGramsLine(nGramDict,line, n)

    return nGramDict

# Counts the n-grams in a line and puts it in a dict
def countNGramsLine(nGramDict, line, n):
    for i in range( len(line) ):
        string = ""
        for j in range(n):
            string += unicode(line[i+j])

        if len(string) == n and string in nGramDict :
            nGramDict[string] += 1
        elif len(string) == n :
            nGramDict[string] = 1
        
        if ( string[n-1] == '>' ):
            break

    return nGramDict

# save to file the n-gram count of nGramDict
def save(output, nGramDict):
    for k, v in sorted(nGramDict.iteritems(), key=lambda (k,v): (-v,k)):
        value = u"{0}\t{1}\n".format(k, v)
        output.write(value)

def main():
    f = codecs.open(sys.argv[1], "r", "utf-8")
    n = int(sys.argv[2])
    o = codecs.open(sys.argv[3], "w", "utf-8")

    nGramDict = countNGrams(f, n)
    save(o, nGramDict)

    f.close()
    o.close()

if __name__ == "__main__":
    main()
