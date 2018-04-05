import unittest2 as unittest
import gameDetector as gd



class TestGameDetector(unittest.TestCase):


    def test(self):
        self.assertEqual(3, 3)


    def testOutput(self):
        gameD = gd.GameDetector()
        self.assertEqual(gameD.getTaggedCorpus(), [])

    def testTuple(self):
        t1= [1,2,3,4]
        tList = [(2,3,4), (1,2,3,4),(3,4,5,6)]
        if tuple(t1) in tList:
            self.assertEqual(3, 3)
        else:
            self.assertEqual(3, 4)

if __name__ == '__main__':
    unittest.main()