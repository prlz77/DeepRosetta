import unittest
from MatconvFileImporter import  Importer
 


class TestImporter(unittest.TestCase):
    def load_file(self,file_path):
        text_file = open(file_path,"r")
        expected_output = text_file.read()
        text_file.close()
        return expected_output


    def testInit(self):
        importer = Importer('../config/Matconv/equivalences.yaml')
        self.assertTrue(importer.equivalences!=None)
    
    def testLoad(self):
        importer = Importer('../config/Matconv/equivalences.yaml')
        output = importer.load('../../resources/imagenet-vgg-s.mat')
       
        #TODO improve output test
        expected_output = self.load_file('../../resources/expected_out.txt')
        self.assertTrue(expected_output==str(output))
        
