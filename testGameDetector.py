import unittest2 as unittest
from gameDetector import GameDetector



class TestGameDetector(unittest.TestCase):

    def setUp(self):
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
        self.gameD = GameDetector(ngramMap, corpus)

    def tearDown(self):
        #self.gameD.dispose()
        self.gameD = None

    def testSampleOutput(self):
        self.assertEqual(self.gameD.getTaggedCorpus(), ['I liked TAG{TAG{Destiny,Destiny}2,the last TAG{Destiny,Destiny} game}, now I play TAG{Fortnite,Fortnite}', 'Lol, no comment about that', "I'm still playing TAG{WorldOfWarcraft,world of warcraft} since ww2"])

    def testEmptyDict(self):
        corpus = ["I liked the last Destiny game, now I play Fortnite", \
                  "Lol, no comment about that" , \
                  "I'm still playing world of warcraft since ww2"]
        self.gameD = GameDetector({}, corpus)
        self.assertEqual(self.gameD.getTaggedCorpus(), corpus)

    def testEmptyCorpus(self):
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
        self.gameD = GameDetector(ngramMap, [])
        self.assertEqual(self.gameD.getTaggedCorpus(), [])


if __name__ == '__main__':
    unittest.main()