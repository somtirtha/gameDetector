


class GameDetector:

    def __init__(self):
        pass

    def getTaggedCorpus(self, ngramMap, corpus):
        return []






if __name__ == '__main__':
    ngramMap = {
                    "CallOfDutyWW2": [ "Call of duty world war two" , "COD WW2" , "COD WWII" , "WW2COD" ],
                    "Fortnite": [ "Fortnite" , "Fort Nite" ],
                    "Destiny": [ "Destiny" , "original Destiny game" ],
                    "Destiny2": [ "Destiny 2" , "the last Destiny game" , "Destiny II" ],
                    "WorldOfWarcraft": [ "WoW the game" , "world of warcraft" ]
                }


    corpus = ["I liked the last Destiny game, now I play Fortnite", \
              "Lol, no comment about that" , \
              "I'm still playing world of warcraft since ww2"]

    gDetector = GameDetector()
    tagCorpus = gDetector.getTaggedCorpus(ngramMap, corpus)
    print tagCorpus


