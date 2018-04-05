import operator


class GameDetector:

    def __init__(self):
        self.processedMapList = []

    def processMapList(self, ngramMap):
        for key, items in ngramMap.items():
            for item in items:
               self.processedMapList.append((key, item, len(item.split(" ")))) 

        self.processedMapList.sort(key=operator.itemgetter(2), reverse=True)


    def findNgrams(self, inputList, n):
        """

        """
        return zip(*[inputList[i:] for i in range(n)])

    def cleanEntry(self, entry):
        """

        """
        entry = entry.lower()
        entryList = entry.split(" " )
        return entryList

    def getTaggedCorpus(self, ngramMap={}, corpus=[]):
        """

        """

        # process map before search
        self.processMapList(ngramMap)

        outputList = []
        # detect ngrams from corpus
        for entry in corpus:
            # clean entry
            cleanList = self.cleanEntry(entry)
            
            idTokenList = []
            for id, token, tokenLength in self.processedMapList:
            # for id, tokenList in ngramMap.items():
                # for token in tokenList:
                    #print(token)

                # find Ngrams depending on the length of the token
                ngrams = list( self.findNgrams(cleanList, tokenLength) )

                # convert token to lower case, splut into words and convert it into a tuple
                tokenTuple = tuple(token.lower().split(" "))

                # tuple present in ngrams append the id and toekn into a list
                if tokenTuple in ngrams:
                    idTokenList.append((id, token))
            
            # replace and append to output list here
            for id, token in idTokenList:
                entry = entry.replace(token, "TAG{" + id + "," + token + "}")
            outputList.append(entry)

        return outputList

"""
eg o/p:
[ "I liked TAG{Destiny2,the last Destiny game}, now I play TAG{Fortnite,Fortnite}" ,
"Lol, no comment about that" ,
...,
"I'm still playing TAG{WorldOfWarcraft,world of warcraft} since ww2" ]
"""


if __name__ == '__main__':
    ngramMap = {
                    "CallOfDutyWW2": [ "Call of duty world war two" , "COD WW2" , "COD WWII" , "WW2COD" ],
                    "Fortnite": [ "Fortnite" , "Fort Nite" ],
                    "Destiny": [ "Destiny" , "original Destiny game" ],
                    "Destiny2": [ "Destiny 2" , "the last Destiny game" , "Destiny II" ],
                    "WorldOfWarcraft": [ "WoW the game" , "world of warcraft" ]
                }

    ngramMap2 = {
                    "Fortnite": [ "Fortnite" , "Fort Nite" ],
                    "Destiny2": [ "Destiny 2" , "the last Destiny game" , "Destiny II" ],
                }


    corpus = ["I liked the last Destiny game, now I play Fortnite", \
              "Lol, no comment about that" , \
              "I'm still playing world of warcraft since ww2"]

    corpus = ["I liked the last Destiny game, now I play Fortnite"]

    gDetector = GameDetector()
    tagCorpus = gDetector.getTaggedCorpus(ngramMap, corpus)
    print(tagCorpus)


