from deep_translator import GoogleTranslator

text = input("Enter text: ")

translated = GoogleTranslator(source="auto", target="hi").translate(text)

print("Translated Text:", translated)