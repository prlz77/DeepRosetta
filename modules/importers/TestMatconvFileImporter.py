import unittest
from MatconvFileImporter import  Importer

class TestImporter(unittest.TestCase):
    def testInit(self):
        importer = Importer('../config/Matconv/equivalences.yaml')
        self.assertTrue(importer.equivalences!=None)
    

