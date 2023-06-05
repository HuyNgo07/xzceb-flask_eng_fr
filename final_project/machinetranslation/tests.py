"""Module test translator"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Class Test Translator"""
    def test_en_fr(self):
        """test translate english to french"""
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('bonjour'), 'hello')

    def test_fr_en(self):
        """test translate english to french"""
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('hello'), 'bonjour')


unittest.main()
