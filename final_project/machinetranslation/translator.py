"""Module translator"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """translate english to french"""
    french_text=MyMemoryTranslator(source='en', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """translate french to english"""
    english_text=MyMemoryTranslator(source='french', target='en').translate(french_text)
    return english_text
