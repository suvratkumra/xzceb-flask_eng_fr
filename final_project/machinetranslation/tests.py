import unittest
from machinetranslation.translator import english_to_french, french_to_english

class Test_Translation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Blue'), 'Bleu')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Noir'), 'Black')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
