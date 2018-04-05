import operator


class GameDetector:
    def __init__(self, _ngramMap={}, _corpus=[]):
        """Constructor fucntion for GameDetector
            Args:
                ngramMap (dict): dictionary containing all ids and tokens \
                                 to be detected
                corpus   (list): list of of all documents to be tagged

        """
        self.ngramMap         = _ngramMap
        self.corpus           = _corpus
        self.processedMapList = []

    #def dispose():


    def processMapList(self, ngramMap):
        """Description: Process map list to create tuples of id, token and \
            length of token in increasing order of lengths and stores in \
            self.processedMapList

            Args: 
                ngramMap (dict): map of game id and the tokens to detect

            Returns:
                None 
        """
        for key, items in ngramMap.items():
            for item in items:
               self.processedMapList.append((key, item, len(item.split(" ")))) 

        self.processedMapList.sort(key=operator.itemgetter(2), reverse=True)


    def findNgrams(self, inputList, n):
        """Find N grams from input list of sentences depending \
            on the value of n

            Args:
                inputList (list): list of each text entry in corpus
                n          (int): the value of the gram \
                                  (number of sunbsequent words)

            Returns:
                list: list of n-grams in that sentence

        """
        return list(zip(*[inputList[i:] for i in range(n)]))


    def cleanEntry(self, entry):
        """Clean each text by converting to lower case and then \
            removing all punctuations that get attached to words \
            and return a list of the words split by space

            eg:
            input: 
            ["I liked the last Destiny game, now I play Fortnite", \
                          "Lol, no comment about that" , \
                          "I'm still playing world of warcraft since ww2"]

            output:
            [ "I liked TAG{Destiny2,the last Destiny game}, now I play 
            TAG{Fortnite,Fortnite}" ,
            "Lol, no comment about that",
            "I'm still playing TAG{WorldOfWarcraft,world of warcraft} since ww2" ]


            Args:
                entry (string): string to be cleaned

            Returns: 
                list: list of the words in the sentence

        """
        entry = entry.lower()
        # remove commas and exclamations
        punctuations = [',', '!', ':', ';']
        for punc in punctuations:
            if punc in entry:
                entry = entry.replace(punc, "")

        entryList = entry.split(" " )
        return entryList

    def getTaggedCorpus(self):
        """Iterate thorugh corpus and tag them depending on 
            the tokens/key words in the dictionary

            Args:
                None

            Returns:
                list: list of the tagged corpus

        """

        # if there is no dictionary
        if(len(self.ngramMap) == 0):
            return self.corpus


        # if there is no corpus
        if(len(self.corpus) == 0):
            return []


        # process map before search
        self.processMapList(self.ngramMap)

        outputList = []
        # detect ngrams from corpus
        for entry in self.corpus:
            # clean entry
            cleanList = self.cleanEntry(entry)
            
            idTokenList = []
            for id, token, tokenLength in self.processedMapList:
                # find Ngrams depending on the length of the token
                ngrams = self.findNgrams(cleanList, tokenLength)

                # convert token to lower case, splut into words and convert \
                # it into a tuple
                tokenTuple = tuple(token.lower().split(" "))

                # tuple present in ngrams append the id and token into a list
                if tokenTuple in ngrams:
                    idTokenList.append((id, token))
            
            # replace and append to output list here
            for id, token in idTokenList:
                tBegIndex = entry.find("TAG{")
                tEndIndex = entry.find("}")
                tokenIndex = entry.find(token)

                # checking to prevent replacing words \
                # inside an already existing tag
                if not (tBegIndex < tokenIndex and tEndIndex > tokenIndex):
                    entry = entry.replace(token, "TAG{" + id + "," + token + "}")
            outputList.append(entry)

        return outputList




if __name__ == '__main__':
    ngramMap = {
                    "CallOfDutyWW2": [ "Call of duty world war two", "COD WW2", \
                    "COD WWII" , "WW2COD" ],
                    "Fortnite": [ "Fortnite" , "Fort Nite" ],
                    "Destiny": [ "Destiny" , "original Destiny game" ],
                    "Destiny2": [ "Destiny 2" , "the last Destiny game", \
                    "Destiny II" ],
                    "WorldOfWarcraft": [ "WoW the game" , \
                    "world of warcraft" ]
                }


    corpus = ["I liked the last Destiny game, now I play Fortnite", \
              "Lol, no comment about that" , \
              "I'm still playing world of warcraft since ww2"]

    # create game detector object
    gDetector = GameDetector(ngramMap, corpus)
    # get tagged corpus
    tagCorpus = gDetector.getTaggedCorpus()
    print(tagCorpus)


