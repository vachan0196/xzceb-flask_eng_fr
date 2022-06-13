"""Unit tests for the translate functions
"""

import unittest
from ..translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Translator class
    """

    def test_english_to_french(self):
        """Tests for the English to French function
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("I love to eat apples."), "J'adore manger des pommes.")
        self.assertEqual(english_to_french(""), "Nothing to Translate")

        self.assertNotEqual(english_to_french("Hello"),"Hello")
        self.assertNotEqual(english_to_french("How are you"),"How are you")

    def test_french_to_english(self):
        """Tests for the French to English function
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("J'adore manger des pommes."), "I love eating apples.")
        self.assertEqual(french_to_english(""), "Rien à Translate")

        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertNotEqual(french_to_english("Comment vous êtes"), "Comment vous êtes")

if __name__ == '__main__':
    unittest.main()
    
